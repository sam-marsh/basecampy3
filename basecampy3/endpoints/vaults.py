import os

from basecampy3.endpoints.recordings import Recording, RecordingEndpoint


class Vault(Recording):

    def vaults(self):
        return self._endpoint.list(self.project_id, self)

    def uploads(self):
        return self._endpoint._api.uploads.list(self.project_id, self)

    def create(self, title):
        return self._endpoint.create(title, self.project_id, self)

    def upload(self, file_path, content_type, base_name=None, description=""):
        name = os.path.basename(file_path)
        if not name:
            base_name = name
        with open(file_path, 'rb') as file:
            attachment = self._endpoint._api.attachments.create(name, file, content_type)
        return self._endpoint._api.uploads.create(self.project_id, self, attachment.attachable_sgid, base_name, description)

    def __int__(self):
        return int(self.id)

    def __str__(self):
        return u"Vault {0.id}: '{0.title}'".format(self)


class Vaults(RecordingEndpoint):
    OBJECT_CLASS = Vault

    CREATE_URL = "{base_url}/buckets/{project_id}/vaults/{vault_id}/vaults.json"
    GET_URL = "{base_url}/buckets/{project_id}/vaults/{vault_id}.json"
    LIST_URL = "{base_url}/buckets/{project_id}/vaults/{vault_id}/vaults.json"
    UPDATE_URL = "{base_url}/buckets/{project_id}/vaults/{vault_id}.json"

    def create(self, title, project, vault):
        data = {
            'title': title,
        }
        project = int(project)
        vault = int(vault)
        url = self.CREATE_URL.format(base_url=self.url, project_id=project, vault_id=vault)
        return self._create(url, data=data)

    def get(self, project, vault):
        project = int(project)
        vault = int(vault)
        url = self.GET_URL.format(base_url=self.url, project_id=project, vault_id=vault)
        return self._get(url)

    def list(self, project, vault):
        project = int(project)
        vault = int(vault)
        url = self.LIST_URL.format(base_url=self.url, project_id=project, vault_id=vault)
        return self._get_list(url)

    def update(self, title, project, vault):
        data = {
            'title': title,
        }
        project = int(project)
        vault = int(vault)
        url = self.UPDATE_URL.format(base_url=self.url, project_id=project, vault_id=vault)
        return self._update(url, data=data)
