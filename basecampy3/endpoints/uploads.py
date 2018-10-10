from .recordings import Recording, RecordingEndpoint


class Upload(Recording):

    def __int__(self):
        return int(self.id)

    def __str__(self):
        return u"Upload {0.id}: '{0.title}'".format(self)


class Uploads(RecordingEndpoint):
    OBJECT_CLASS = Upload

    LIST_URL = "{base_url}/buckets/{project_id}/vaults/{vault_id}/uploads.json"
    GET_URL = "{base_url}/buckets/{project_id}/uploads/{upload_id}.json"
    CREATE_URL = "{base_url}/buckets/{project_id}/vaults/{vault_id}/uploads.json"
    UPDATE_URL = "{base_url}/buckets/{project_id}/uploads/{upload_id}.json"

    def list(self, project, vault):
        project = int(project)
        vault = int(vault)
        url = self.LIST_URL.format(base_url=self.url, project_id=project, vault_id=vault)
        return self._get_list(url)

    def get(self, project, upload):
        project = int(project)
        upload = int(upload)
        url = self.GET_URL.format(base_url=self.url, project_id=project, upload_id=upload)
        return self._get(url)

    def create(self, project, vault, attachment, name, description=""):
        data = {
            'attachable_sgid': attachment,
            'base_name': name,
            'description': description
        }
        project = int(project)
        vault = int(vault)
        url = self.CREATE_URL.format(base_url=self.url, project_id=project, vault_id=vault)
        return self._create(url, data=data)

    def update(self, project, upload, name, description=""):
        data = {
            'base_name': name,
            'description': description
        }
        project = int(project)
        upload = int(upload)
        url = self.UPDATE_URL.format(base_url=self.url, project_id=project, upload_id=upload)
        return self._create(url, data=data)
