# Changelog

All notable changes to the Connect API will be documented here.

## [2023-11-29]

### Changed

- Update endpoints `GET /connect/v1/rate-bundle` and `POST /connect/v1/preview` to include contract volume information
if configured


## [2023-10-06]

### Added

- Endpoint to get relevant studio information for cancellation page (`GET /connect/v1/contracts/studios/{studioId}`)
containing cancellation reasons and legal information


### Deprecated

- Deprecate endpoint for cancellation reasons (`GET /connect/v1/contracts/studios/{studioId}/cancellation-reasons`) for
contract cancellations


## [2023-08-16]

### Added

- Add more efficient endpoints to load studios (`GET /connect/v2/contracts/studios`) and cancellation
reasons (`GET /connect/v1/contracts/studios/{studioId}/cancellation-reasons`) for contract cancellations


### Deprecated

- Deprecate endpoint `GET /connect/v1/contracts/studios` for loading studios along with cancellation reasons in a
contract cancellation context. Instead, the endpoint `GET /connect/v2/contracts/studios` shall be used to load basic
studio information and the endpoint `GET /connect/v1/contracts/studios/{studioId}/cancellation-reasons` shall be used
to load the cancellation reasons for a specific studio.


## [2023-03-07]

### Added

- Add field for privacy configuration to trial session booking inside the lead customer DTO


### Changed

## [2023-02-14]

### Added

- Add endpoints for voucher discount information and redeeming


### Changed

## [2022-12-16]

### Added

- Add endpoints for online cancellations


### Changed

- Enhance information about default page for online cancellations