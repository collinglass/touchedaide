
## Back-end API

### GET /api/activities/

#### Params

filters:

 * **policy**: iati_code
 * **country**: iati_code

#### Returns

```json
[
  {
    "iati_code": "iati code",
    "date": {
      "start": "iso date",
      "end": "iso date"
    },
    "policy": {
      "iati_code": "code",
      "en": "english code name",
      "fr": "french code name"
    },
    "country": {
      "iati_code": "code",
      "en": "english country name",
      "fr": "french country name"
    },
    "organization": {
      "iati_code": "code",
      "en": "english org name",
      "fr": "french org name"
    }
  },
  .
  .
  .
]

```
