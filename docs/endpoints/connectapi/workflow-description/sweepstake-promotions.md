# Sweepstake promotions

## Configuration

Magicline customers can configure promotions which will be then presented to their members. One type of promotion could
be a sweepstake which will direct the member to an external page where detailed information can be found and the
legal consent can be accepted.

## Participation

When the member is redirected to the external page, the URL param `payload` is added to that URL, e.g.
`https://www.mylandingpage.com?payload=C1AAHwYTAAFMaUchMys6DjdbXFAMGBwABgILISwHUF9FeFROQUZfX1tERU0eIQoOHREdJAswFFBVXFxFUVlWYVZVQklWJQoNGRQGDg4AAAAAGgFBSAsBJwkE`

If the member participated, the same payload needs to be sent back via this [endpoint](/apis/magicline/connectapi/connectapi#operation/confirmCustomerParticipation):

`POST /connect/v1/promotion/confirm-participation?payload=<payload>`

This marks the member as a participant on Magicline side. Any success message must be presented by the landingpage
as long as the endpoint returns 200 as response code. The member then can close the page.