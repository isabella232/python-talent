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

from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.talent_v4beta1.types import job
from google.cloud.talent_v4beta1.types import job as gct_job
from google.cloud.talent_v4beta1.types import job_service
from google.longrunning import operations_pb2 as operations  # type: ignore
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import JobServiceTransport
from .grpc import JobServiceGrpcTransport


class JobServiceGrpcAsyncIOTransport(JobServiceTransport):
    """gRPC AsyncIO backend transport for JobService.

    A service handles job management, including job CRUD,
    enumeration and search.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "jobs.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "jobs.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
        )

        self._stubs = {}

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channel = self.create_channel(
                self._host, credentials=self._credentials,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if "operations_client" not in self.__dict__:
            self.__dict__["operations_client"] = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__["operations_client"]

    @property
    def create_job(
        self,
    ) -> Callable[[job_service.CreateJobRequest], Awaitable[gct_job.Job]]:
        r"""Return a callable for the create job method over gRPC.

        Creates a new job.
        Typically, the job becomes searchable within 10 seconds,
        but it may take up to 5 minutes.

        Returns:
            Callable[[~.CreateJobRequest],
                    Awaitable[~.Job]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_job" not in self._stubs:
            self._stubs["create_job"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/CreateJob",
                request_serializer=job_service.CreateJobRequest.serialize,
                response_deserializer=gct_job.Job.deserialize,
            )
        return self._stubs["create_job"]

    @property
    def batch_create_jobs(
        self,
    ) -> Callable[
        [job_service.BatchCreateJobsRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch create jobs method over gRPC.

        Begins executing a batch create jobs operation.

        Returns:
            Callable[[~.BatchCreateJobsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_jobs" not in self._stubs:
            self._stubs["batch_create_jobs"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/BatchCreateJobs",
                request_serializer=job_service.BatchCreateJobsRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_create_jobs"]

    @property
    def get_job(self) -> Callable[[job_service.GetJobRequest], Awaitable[job.Job]]:
        r"""Return a callable for the get job method over gRPC.

        Retrieves the specified job, whose status is OPEN or
        recently EXPIRED within the last 90 days.

        Returns:
            Callable[[~.GetJobRequest],
                    Awaitable[~.Job]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_job" not in self._stubs:
            self._stubs["get_job"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/GetJob",
                request_serializer=job_service.GetJobRequest.serialize,
                response_deserializer=job.Job.deserialize,
            )
        return self._stubs["get_job"]

    @property
    def update_job(
        self,
    ) -> Callable[[job_service.UpdateJobRequest], Awaitable[gct_job.Job]]:
        r"""Return a callable for the update job method over gRPC.

        Updates specified job.
        Typically, updated contents become visible in search
        results within 10 seconds, but it may take up to 5
        minutes.

        Returns:
            Callable[[~.UpdateJobRequest],
                    Awaitable[~.Job]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_job" not in self._stubs:
            self._stubs["update_job"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/UpdateJob",
                request_serializer=job_service.UpdateJobRequest.serialize,
                response_deserializer=gct_job.Job.deserialize,
            )
        return self._stubs["update_job"]

    @property
    def batch_update_jobs(
        self,
    ) -> Callable[
        [job_service.BatchUpdateJobsRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch update jobs method over gRPC.

        Begins executing a batch update jobs operation.

        Returns:
            Callable[[~.BatchUpdateJobsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_jobs" not in self._stubs:
            self._stubs["batch_update_jobs"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/BatchUpdateJobs",
                request_serializer=job_service.BatchUpdateJobsRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_update_jobs"]

    @property
    def delete_job(
        self,
    ) -> Callable[[job_service.DeleteJobRequest], Awaitable[empty.Empty]]:
        r"""Return a callable for the delete job method over gRPC.

        Deletes the specified job.
        Typically, the job becomes unsearchable within 10
        seconds, but it may take up to 5 minutes.

        Returns:
            Callable[[~.DeleteJobRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_job" not in self._stubs:
            self._stubs["delete_job"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/DeleteJob",
                request_serializer=job_service.DeleteJobRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_job"]

    @property
    def batch_delete_jobs(
        self,
    ) -> Callable[[job_service.BatchDeleteJobsRequest], Awaitable[empty.Empty]]:
        r"""Return a callable for the batch delete jobs method over gRPC.

        Deletes a list of [Job][google.cloud.talent.v4beta1.Job]s by
        filter.

        Returns:
            Callable[[~.BatchDeleteJobsRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_jobs" not in self._stubs:
            self._stubs["batch_delete_jobs"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/BatchDeleteJobs",
                request_serializer=job_service.BatchDeleteJobsRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["batch_delete_jobs"]

    @property
    def list_jobs(
        self,
    ) -> Callable[
        [job_service.ListJobsRequest], Awaitable[job_service.ListJobsResponse]
    ]:
        r"""Return a callable for the list jobs method over gRPC.

        Lists jobs by filter.

        Returns:
            Callable[[~.ListJobsRequest],
                    Awaitable[~.ListJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_jobs" not in self._stubs:
            self._stubs["list_jobs"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/ListJobs",
                request_serializer=job_service.ListJobsRequest.serialize,
                response_deserializer=job_service.ListJobsResponse.deserialize,
            )
        return self._stubs["list_jobs"]

    @property
    def search_jobs(
        self,
    ) -> Callable[
        [job_service.SearchJobsRequest], Awaitable[job_service.SearchJobsResponse]
    ]:
        r"""Return a callable for the search jobs method over gRPC.

        Searches for jobs using the provided
        [SearchJobsRequest][google.cloud.talent.v4beta1.SearchJobsRequest].

        This call constrains the
        [visibility][google.cloud.talent.v4beta1.Job.visibility] of jobs
        present in the database, and only returns jobs that the caller
        has permission to search against.

        Returns:
            Callable[[~.SearchJobsRequest],
                    Awaitable[~.SearchJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_jobs" not in self._stubs:
            self._stubs["search_jobs"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/SearchJobs",
                request_serializer=job_service.SearchJobsRequest.serialize,
                response_deserializer=job_service.SearchJobsResponse.deserialize,
            )
        return self._stubs["search_jobs"]

    @property
    def search_jobs_for_alert(
        self,
    ) -> Callable[
        [job_service.SearchJobsRequest], Awaitable[job_service.SearchJobsResponse]
    ]:
        r"""Return a callable for the search jobs for alert method over gRPC.

        Searches for jobs using the provided
        [SearchJobsRequest][google.cloud.talent.v4beta1.SearchJobsRequest].

        This API call is intended for the use case of targeting passive
        job seekers (for example, job seekers who have signed up to
        receive email alerts about potential job opportunities), and has
        different algorithmic adjustments that are targeted to passive
        job seekers.

        This call constrains the
        [visibility][google.cloud.talent.v4beta1.Job.visibility] of jobs
        present in the database, and only returns jobs the caller has
        permission to search against.

        Returns:
            Callable[[~.SearchJobsRequest],
                    Awaitable[~.SearchJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_jobs_for_alert" not in self._stubs:
            self._stubs["search_jobs_for_alert"] = self.grpc_channel.unary_unary(
                "/google.cloud.talent.v4beta1.JobService/SearchJobsForAlert",
                request_serializer=job_service.SearchJobsRequest.serialize,
                response_deserializer=job_service.SearchJobsResponse.deserialize,
            )
        return self._stubs["search_jobs_for_alert"]


__all__ = ("JobServiceGrpcAsyncIOTransport",)