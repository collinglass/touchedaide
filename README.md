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

### GET /api/activities/<iati_code>

#### Params

none for now.

#### Returns

```json
{
  "iati_code": "code",
  "title": "string",
  "date": {
    "start": "iso date",
    "end": "iso date"
  },
  "policy": [
    {
      "iati_code": "code",
      "en": "english name",
      "fr": "french name",
      "significance": "int (0 - 3; not significant - exclusive focus)"
    },
    ...
  ],
  "country": {
    "iati_code": "code",
    "en": "english name",
    "fr": "french name"
  },
  "organization": {
    "iati_code": "code",
    "en": "english name",
    "fr": "french name"
  },
  "description": {
    "en": "english description",
    "fr": "french description"
  }
}
```




