# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.talent_v4.services.job_service import pagers
from google.cloud.talent_v4.types import common
from google.cloud.talent_v4.types import histogram
from google.cloud.talent_v4.types import job
from google.cloud.talent_v4.types import job as gct_job
from google.cloud.talent_v4.types import job_service
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore

from .transports.base import JobServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import JobServiceGrpcAsyncIOTransport
from .client import JobServiceClient


class JobServiceAsyncClient:
    """A service handles job management, including job CRUD,
    enumeration and search.
    """

    _client: JobServiceClient

    DEFAULT_ENDPOINT = JobServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = JobServiceClient.DEFAULT_MTLS_ENDPOINT

    job_path = staticmethod(JobServiceClient.job_path)
    parse_job_path = staticmethod(JobServiceClient.parse_job_path)

    from_service_account_file = JobServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    get_transport_class = functools.partial(
        type(JobServiceClient).get_transport_class, type(JobServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, JobServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the job service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.JobServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = JobServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_job(
        self,
        request: job_service.CreateJobRequest = None,
        *,
        parent: str = None,
        job: gct_job.Job = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gct_job.Job:
        r"""Creates a new job.
        Typically, the job becomes searchable within 10 seconds,
        but it may take up to 5 minutes.

        Args:
            request (:class:`~.job_service.CreateJobRequest`):
                The request object. Create job request.
            parent (:class:`str`):
                Required. The resource name of the tenant under which
                the job is created.

                The format is
                "projects/{project_id}/tenants/{tenant_id}". For
                example, "projects/foo/tenants/bar".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job (:class:`~.gct_job.Job`):
                Required. The Job to be created.
                This corresponds to the ``job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.gct_job.Job:
                A Job resource represents a job posting (also referred
                to as a "job listing" or "job requisition"). A job
                belongs to a [Company][google.cloud.talent.v4.Company],
                which is the hiring entity responsible for the job.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, job]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.CreateJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if job is not None:
            request.job = job

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_job,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def batch_create_jobs(
        self,
        request: job_service.BatchCreateJobsRequest = None,
        *,
        parent: str = None,
        jobs: Sequence[job.Job] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Begins executing a batch create jobs operation.

        Args:
            request (:class:`~.job_service.BatchCreateJobsRequest`):
                The request object. Request to create a batch of jobs.
            parent (:class:`str`):
                Required. The resource name of the tenant under which
                the job is created.

                The format is
                "projects/{project_id}/tenants/{tenant_id}". For
                example, "projects/foo/tenants/bar".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            jobs (:class:`Sequence[~.job.Job]`):
                Required. The jobs to be created.
                A maximum of 200 jobs can be created in
                a batch.
                This corresponds to the ``jobs`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.job_service.BatchCreateJobsResponse``: The
                result of
                [JobService.BatchCreateJobs][google.cloud.talent.v4.JobService.BatchCreateJobs].
                It's used to replace
                [google.longrunning.Operation.response][google.longrunning.Operation.response]
                in case of success.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, jobs]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.BatchCreateJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if jobs is not None:
            request.jobs = jobs

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_create_jobs,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            job_service.BatchCreateJobsResponse,
            metadata_type=common.BatchOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_job(
        self,
        request: job_service.GetJobRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> job.Job:
        r"""Retrieves the specified job, whose status is OPEN or
        recently EXPIRED within the last 90 days.

        Args:
            request (:class:`~.job_service.GetJobRequest`):
                The request object. Get job request.
            name (:class:`str`):
                Required. The resource name of the job to retrieve.

                The format is
                "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}".
                For example, "projects/foo/tenants/bar/jobs/baz".
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.job.Job:
                A Job resource represents a job posting (also referred
                to as a "job listing" or "job requisition"). A job
                belongs to a [Company][google.cloud.talent.v4.Company],
                which is the hiring entity responsible for the job.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.GetJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_job,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                ),
            ),
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_job(
        self,
        request: job_service.UpdateJobRequest = None,
        *,
        job: gct_job.Job = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gct_job.Job:
        r"""Updates specified job.
        Typically, updated contents become visible in search
        results within 10 seconds, but it may take up to 5
        minutes.

        Args:
            request (:class:`~.job_service.UpdateJobRequest`):
                The request object. Update job request.
            job (:class:`~.gct_job.Job`):
                Required. The Job to be updated.
                This corresponds to the ``job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
                Strongly recommended for the best service experience.

                If
                [update_mask][google.cloud.talent.v4.UpdateJobRequest.update_mask]
                is provided, only the specified fields in
                [job][google.cloud.talent.v4.UpdateJobRequest.job] are
                updated. Otherwise all the fields are updated.

                A field mask to restrict the fields that are updated.
                Only top level fields of
                [Job][google.cloud.talent.v4.Job] are supported.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.gct_job.Job:
                A Job resource represents a job posting (also referred
                to as a "job listing" or "job requisition"). A job
                belongs to a [Company][google.cloud.talent.v4.Company],
                which is the hiring entity responsible for the job.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([job, update_mask]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.UpdateJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if job is not None:
            request.job = job
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_job,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("job.name", request.job.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def batch_update_jobs(
        self,
        request: job_service.BatchUpdateJobsRequest = None,
        *,
        parent: str = None,
        jobs: Sequence[job.Job] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Begins executing a batch update jobs operation.

        Args:
            request (:class:`~.job_service.BatchUpdateJobsRequest`):
                The request object. Request to update a batch of jobs.
            parent (:class:`str`):
                Required. The resource name of the tenant under which
                the job is created.

                The format is
                "projects/{project_id}/tenants/{tenant_id}". For
                example, "projects/foo/tenants/bar".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            jobs (:class:`Sequence[~.job.Job]`):
                Required. The jobs to be updated.
                A maximum of 200 jobs can be updated in
                a batch.
                This corresponds to the ``jobs`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.job_service.BatchUpdateJobsResponse``: The
                result of
                [JobService.BatchUpdateJobs][google.cloud.talent.v4.JobService.BatchUpdateJobs].
                It's used to replace
                [google.longrunning.Operation.response][google.longrunning.Operation.response]
                in case of success.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, jobs]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.BatchUpdateJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if jobs is not None:
            request.jobs = jobs

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_update_jobs,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            job_service.BatchUpdateJobsResponse,
            metadata_type=common.BatchOperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_job(
        self,
        request: job_service.DeleteJobRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified job.
        Typically, the job becomes unsearchable within 10
        seconds, but it may take up to 5 minutes.

        Args:
            request (:class:`~.job_service.DeleteJobRequest`):
                The request object. Delete job request.
            name (:class:`str`):
                Required. The resource name of the job to be deleted.

                The format is
                "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}".
                For example, "projects/foo/tenants/bar/jobs/baz".
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.DeleteJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_job,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                ),
            ),
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def batch_delete_jobs(
        self,
        request: job_service.BatchDeleteJobsRequest = None,
        *,
        parent: str = None,
        names: Sequence[str] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Begins executing a batch delete jobs operation.

        Args:
            request (:class:`~.job_service.BatchDeleteJobsRequest`):
                The request object. Request to delete a batch of jobs.
            parent (:class:`str`):
                Required. The resource name of the tenant under which
                the job is created.

                The format is
                "projects/{project_id}/tenants/{tenant_id}". For
                example, "projects/foo/tenants/bar".

                The parent of all of the jobs specified in ``names``
                must match this field.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (:class:`Sequence[str]`):
                The names of the jobs to delete.

                The format is
                "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}".
                For example, "projects/foo/tenants/bar/jobs/baz".

                A maximum of 200 jobs can be deleted in a batch.
                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.job_service.BatchDeleteJobsResponse``: The
                result of
                [JobService.BatchDeleteJobs][google.cloud.talent.v4.JobService.BatchDeleteJobs].
                It's used to replace
                [google.longrunning.Operation.response][google.longrunning.Operation.response]
                in case of success.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, names]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.BatchDeleteJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if names is not None:
            request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_delete_jobs,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            job_service.BatchDeleteJobsResponse,
            metadata_type=common.BatchOperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_jobs(
        self,
        request: job_service.ListJobsRequest = None,
        *,
        parent: str = None,
        filter: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListJobsAsyncPager:
        r"""Lists jobs by filter.

        Args:
            request (:class:`~.job_service.ListJobsRequest`):
                The request object. List jobs request.
            parent (:class:`str`):
                Required. The resource name of the tenant under which
                the job is created.

                The format is
                "projects/{project_id}/tenants/{tenant_id}". For
                example, "projects/foo/tenants/bar".
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Required. The filter string specifies the jobs to be
                enumerated.

                Supported operator: =, AND

                The fields eligible for filtering are:

                -  ``companyName`` (Required)
                -  ``requisitionId``
                -  ``status`` Available values: OPEN, EXPIRED, ALL.
                   Defaults to OPEN if no value is specified.

                Sample Query:

                -  companyName =
                   "projects/foo/tenants/bar/companies/baz"
                -  companyName =
                   "projects/foo/tenants/bar/companies/baz" AND
                   requisitionId = "req-1"
                -  companyName =
                   "projects/foo/tenants/bar/companies/baz" AND status =
                   "EXPIRED".
                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListJobsAsyncPager:
                List jobs response.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, filter]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = job_service.ListJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_jobs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    exceptions.ServiceUnavailable, exceptions.DeadlineExceeded,
                ),
            ),
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListJobsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_jobs(
        self,
        request: job_service.SearchJobsRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> job_service.SearchJobsResponse:
        r"""Searches for jobs using the provided
        [SearchJobsRequest][google.cloud.talent.v4.SearchJobsRequest].

        This call constrains the
        [visibility][google.cloud.talent.v4.Job.visibility] of jobs
        present in the database, and only returns jobs that the caller
        has permission to search against.

        Args:
            request (:class:`~.job_service.SearchJobsRequest`):
                The request object. The Request body of the `SearchJobs`
                call.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.job_service.SearchJobsResponse:
                Response for SearchJob method.
        """
        # Create or coerce a protobuf request object.

        request = job_service.SearchJobsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_jobs,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def search_jobs_for_alert(
        self,
        request: job_service.SearchJobsRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> job_service.SearchJobsResponse:
        r"""Searches for jobs using the provided
        [SearchJobsRequest][google.cloud.talent.v4.SearchJobsRequest].

        This API call is intended for the use case of targeting passive
        job seekers (for example, job seekers who have signed up to
        receive email alerts about potential job opportunities), it has
        different algorithmic adjustments that are designed to
        specifically target passive job seekers.

        This call constrains the
        [visibility][google.cloud.talent.v4.Job.visibility] of jobs
        present in the database, and only returns jobs the caller has
        permission to search against.

        Args:
            request (:class:`~.job_service.SearchJobsRequest`):
                The request object. The Request body of the `SearchJobs`
                call.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.job_service.SearchJobsResponse:
                Response for SearchJob method.
        """
        # Create or coerce a protobuf request object.

        request = job_service.SearchJobsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_jobs_for_alert,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-talent",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("JobServiceAsyncClient",)
