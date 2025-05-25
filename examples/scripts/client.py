# /qompassai/radar/examples/scripts/client.py
# -----------------------------------
# Copyright (C) 2025 Qompass AI, All rights reserved
from __future__ import annotations

import os
from pathlib import Path
from posixpath import join as urljoin
from typing import Any
from urllib.parse import urlparse, urlunparse

import requests


class RadarClient(object):
    def __init__(self, address: str | None = None, api_version: str = "v0") -> None:
        address = (
            f"{address}/api/{api_version}"
            if address
            else f"{os.environ['RADAR_RESTAPI_URI']}/api/{api_version}"
        )
        self._scheme, self._netloc, self._path, _, _, _ = urlparse(address)

    @property
    def experiment_endpoint(self) -> str:
        return urlunparse(
            (self._scheme, self._netloc, urljoin(self._path, "experiment/"), "", "", "")
        )

    @property
    def job_endpoint(self) -> str:
        return urlunparse(
            (self._scheme, self._netloc, urljoin(self._path, "job/"), "", "", "")
        )

    @property
    def task_plugin_endpoint(self) -> str:
        return urlunparse(
            (self._scheme, self._netloc, urljoin(self._path, "taskPlugin/"), "", "", "")
        )

    @property
    def task_plugin_builtins_endpoint(self) -> str:
        return urlunparse(
            (
                self._scheme,
                self._netloc,
                urljoin(self._path, "taskPlugin/radar_builtins"),
                "",
                "",
                "",
            )
        )

    @property
    def task_plugin_custom_endpoint(self) -> str:
        return urlunparse(
            (
                self._scheme,
                self._netloc,
                urljoin(self._path, "taskPlugin/radar_custom"),
                "",
                "",
                "",
            )
        )

    @property
    def queue_endpoint(self) -> str:
        return urlunparse(
            (self._scheme, self._netloc, urljoin(self._path, "queue/"), "", "", "")
        )

    def delete_custom_task_plugin(self, name: str):
        plugin_name_query: str = urljoin(self.task_plugin_custom_endpoint, name)
        return requests.delete(plugin_name_query).json()

    def get_experiment_by_id(self, id: int):
        experiment_id_query: str = urljoin(self.experiment_endpoint, str(id))
        return requests.get(experiment_id_query).json()

    def get_experiment_by_name(self, name: str):
        experiment_name_query: str = urljoin(self.experiment_endpoint, "name", name)
        return requests.get(experiment_name_query).json()

    def get_job_by_id(self, id: str):
        job_id_query: str = urljoin(self.job_endpoint, id)
        return requests.get(job_id_query).json()

    def get_queue_by_id(self, id: int):
        queue_id_query: str = urljoin(self.queue_endpoint, str(id))
        return requests.get(queue_id_query).json()

    def get_queue_by_name(self, name: str):
        queue_name_query: str = urljoin(self.queue_endpoint, "name", name)
        return requests.get(queue_name_query).json()

    def get_builtin_task_plugin(self, name: str):
        task_plugin_name_query: str = urljoin(self.task_plugin_builtins_endpoint, name)
        return requests.get(task_plugin_name_query).json()

    def get_custom_task_plugin(self, name: str):
        task_plugin_name_query: str = urljoin(self.task_plugin_custom_endpoint, name)
        return requests.get(task_plugin_name_query).json()

    def list_experiments(self) -> list[dict[str, Any]]:
        return requests.get(self.experiment_endpoint).json()

    def list_jobs(self) -> list[dict[str, Any]]:
        return requests.get(self.job_endpoint).json()

    def list_queues(self) -> list[dict[str, Any]]:
        return requests.get(self.queue_endpoint).json()

    def list_all_task_plugins(self) -> list[dict[str, Any]]:
        return requests.get(self.task_plugin_endpoint).json()

    def list_builtin_task_plugins(self) -> list[dict[str, Any]]:
        return requests.get(self.task_plugin_builtins_endpoint).json()

    def list_custom_task_plugins(self) -> list[dict[str, Any]]:
        return requests.get(self.task_plugin_custom_endpoint).json()

    def lock_queue(self, name: str):
        queue_name_query: str = urljoin(self.queue_endpoint, "name", name, "lock")
        return requests.put(queue_name_query).json()

    def unlock_queue(self, name: str):
        queue_name_query: str = urljoin(self.queue_endpoint, "name", name, "lock")
        return requests.delete(queue_name_query).json()

    def register_experiment(self, name: str) -> dict[str, Any]:
        experiment_registration_form = {"name": name}

        response = requests.post(
            self.experiment_endpoint,
            json=experiment_registration_form,
        )

        return response.json()

    def register_queue(self, name: str = "tensorflow_cpu") -> dict[str, Any]:
        queue_registration_form = {"name": name}

        response = requests.post(
            self.queue_endpoint,
            json=queue_registration_form,
        )

        return response.json()

    def submit_job(
        self,
        workflows_file: str | Path,
        experiment_name: str,
        entry_point: str,
        entry_point_kwargs: str | None = None,
        depends_on: str | None = None,
        queue: str = "tensorflow_cpu",
        timeout: str = "24h",
    ) -> dict[str, Any]:
        job_form: dict[str, Any] = {
            "experimentName": experiment_name,
            "queue": queue,
            "timeout": timeout,
            "entryPoint": entry_point,
        }

        if entry_point_kwargs is not None:
            job_form["entryPointKwargs"] = entry_point_kwargs

        if depends_on is not None:
            job_form["dependsOn"] = depends_on

        workflows_file = Path(workflows_file)

        with workflows_file.open("rb") as f:
            job_files = {"workflow": (workflows_file.name, f)}
            response = requests.post(
                self.job_endpoint,
                data=job_form,
                files=job_files,
            )

        return response.json()

    def upload_custom_plugin_package(
        self,
        custom_plugin_name: str,
        custom_plugin_file: str | Path,
        collection: str = "radar_custom",
    ) -> dict[str, Any]:
        plugin_upload_form = {
            "taskPluginName": custom_plugin_name,
            "collection": collection,
        }

        custom_plugin_file = Path(custom_plugin_file)

        with custom_plugin_file.open("rb") as f:
            custom_plugin_file = {"taskPluginFile": (custom_plugin_file.name, f)}
            response = requests.post(
                self.task_plugin_endpoint,
                data=plugin_upload_form,
                files=custom_plugin_file,
            )

        return response.json()
