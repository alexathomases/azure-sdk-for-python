from deid_base_test_case import *
from devtools_testutils import (
    recorded_by_proxy,
)

from azure.health.deidentification.models import *
from azure.core.polling import LROPoller


class TestHealthDeidentificationCreateAndListJob(DeidBaseTestCase):
    @BatchEnv()
    @recorded_by_proxy
    def test_create_list(self, **kwargs):
        endpoint: str = kwargs.pop("healthdataaiservices_deid_service_endpoint")
        inputPrefix = "example_patient_1"
        storage_location: str = self.get_storage_location(kwargs)
        client = self.make_client(endpoint)
        assert client is not None

        jobname = self.generate_job_name()

        job = DeidentificationJob(
            source_location=SourceStorageLocation(
                location=storage_location,
                prefix=inputPrefix,
            ),
            target_location=TargetStorageLocation(location=storage_location, prefix=self.OUTPUT_PATH, overwrite=True),
            operation=DeidentificationOperationType.REDACT,
            customizations=DeidentificationJobCustomizationOptions(redaction_format="[{type}]"),
        )

        client.begin_deidentify_documents(jobname, job)
        jobs = client.list_jobs()

        job = None
        jobsToLookThrough = 10
        for j in jobs:
            jobsToLookThrough -= 1
            if j.name == jobname:
                job = j
                break
            elif jobsToLookThrough <= 0:
                raise Exception("Job not found in list_jobs")

        assert job is not None
        assert job.name == jobname
        assert job.status == DeidentificationJobStatus.NOT_STARTED or job.status == DeidentificationJobStatus.RUNNING
        assert job.operation == DeidentificationOperationType.REDACT
        assert job.error is None
        assert job.created_at is not None
        assert job.last_updated_at is not None
        assert job.customizations is not None
        assert job.customizations.redaction_format == "[{type}]"
