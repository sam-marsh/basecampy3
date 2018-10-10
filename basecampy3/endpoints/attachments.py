from ._base import BasecampObject, BasecampEndpoint, Basecamp3Error


class Attachment(BasecampObject):

    def __str__(self):
        return u"Attachment {0.attachable_sgid}".format(self)


class Attachments(BasecampEndpoint):
    OBJECT_CLASS = Attachment

    CREATE_URL = "{base_url}/attachments.json?name={file_name}"

    def create(self, name, file, content_type):
        url = self.CREATE_URL.format(base_url=self.url, file_name=name)
        resp = self._api._session.post(url, files={'data': (name, file, content_type)})
        if not resp.ok:
            raise Basecamp3Error(response=resp)
        json_data = resp.json()
        object_class = self.OBJECT_CLASS
        item = object_class(json_data, self)
        return item
