from SiemplifyJob import SiemplifyJob

INTEGRATION_NAME = "MyIntegration2"
SCRIPT_NAME = "JobTemplate"


def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME # In order to use the SiemplifyLogger, you must assign a name to the script.
    
    # INIT INTEGRATION CONFIGURATION:
    integration_param = siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,param_name="Param A")


    # INIT ACTION PARAMETERS:
    job_param = siemplify.extract_job_param(param_name="Param C", print_value=True)


    try:
        pass
        # .... CUSTOM LOGIC HERE....
        # .... CUSTOM LOGIC HERE....
        # .... CUSTOM LOGIC HERE....

    except Exception as e:
        siemplify.LOGGER.error("General error performing Job {}".format(SCRIPT_NAME))
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()