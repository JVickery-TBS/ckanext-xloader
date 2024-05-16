from ckan.plugins.interfaces import Interface


class IXloader(Interface):
    """
    The IXloader interface allows plugin authors to receive notifications
    before and after a resource is submitted to the xloader service, as
    well as determining whether a resource should be submitted in can_upload

    The before_submit function, when implemented
    """

    def can_upload(self, resource_id):
        """ This call when implemented can be used to stop the processing of
        the xloader submit function. This method will not be called if
        the resource format does not match those defined in the
        ckanext.xloader.formats config option or the default formats.

        If this function returns False then processing will be aborted,
        whilst returning True will submit the resource to the xloader
        service

        Note that before reaching this hook there is a prior check on the
        resource format, which depends on the value of
        the :ref:`ckanext.xloader.formats` configuration option (and requires
        the resource to have a format defined).

        :param resource_id: The ID of the resource that is to be
            pushed to the xloader service.

        Returns ``True`` if the job should be submitted and ``False`` if
        the job should be aborted

        :rtype: bool
        """
        return True

    def after_upload(self, context, resource_dict, dataset_dict):
        """ After a resource has been successfully upload to the datastore
        this method will be called with the resource dictionary and the
        package dictionary for this resource.

        :param context: The context within which the upload happened
        :param resource_dict: The dict represenstaion of the resource that was
            successfully uploaded to the datastore
        :param dataset_dict: The dict represenstation of the dataset containing
            the resource that was uploaded
        """
        pass


class IPipeXloader(Interface):
    """
    Process data in a Data Pipeline.

    Inherit this to subscribe to events in the Data Pipeline and be able to
    broadcast the results for others to process next. In this way, a number of
    IPipes can be linked up in sequence to build up a data processing pipeline.

    When a resource is xloadered, it broadcasts its status in the DataStore,
    perhaps triggering a process which notifies users of the status.
    These processes can in turn put the resulting resource DS status into the pipeline
    """

    def receive_xloader_status(self, xloader_status):
        pass
