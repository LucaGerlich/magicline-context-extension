# Connect API

Use this API to integrate online contract concluding, trial session booking and/or lead forms into your own website.
For troubleshooting also see our [FAQ](/apis/magicline/connectapi/faq)

## Prerequisites

- Check that the Connect API is enabled for you Magicline license. In doubt contact our support.
- Configure contract offers (rate bundles)
- Add these offers to the offer group named Connect API


## Access the API

The host name for the API contains the name of your Magicline tenant.
E.g. this documentation is connected to the Magicline demo tenant `connectdemo`

If you want to start the integration into your productive website the host name must be adapted to the matching tenant:

`https://<tenant_name>.api.magicline.com`

e.g. the [URL for fetching studios](/apis/magicline/connectapi/connectapi#operation/getStudioList) would look like this:

`https://<tenant_name>.api.magicline.com/connect/v1/studio`