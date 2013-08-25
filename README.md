# 2013 Citizen Attaché Hackathon
*Ottawa on International Aid, Visualization Team*

## Set-up
### Front-end

#### How to set up Sass and Compass on your machine:

If you don't have Ruby or Sass installed yet, grab 'em. In terminal:
```bash
sudo apt-get install ruby-full rubygems1.8
sudo gem install sass
sudo gem install compass
```
Switch to the dev folder:
```bash
cd path/to/cdndevhack/
```
And tell compass to watch the project!
```bash
compass watch
```
For reference (i.e. you *don't* need to do this!), the command that I used to set up compass in this directory was:
```bash
compass create --syntax sass --sass-dir "static/stylesheets/sass" --css-dir "static/stylesheets/css" --javascripts-dir "static/js" --images-dir "static/img"
```
I grabbed it [here](http://compass-style.org/install/).

#### Emmet stuff
While we're still working on dummy markup, if you want to make tweaks to the **1000 line** behemoth just change the following and run it through [emmet](http://docs.emmet.io/):
```emmet
nav>ul>li*4>h2{Year}+ul>li*12>h3{Month}+ul>li*3>img.icon[src="demoIcon.png"]+time{2013-08-01}+{$3M Columbia}+h4{Agriculture}
```

## Back-end API


### GET /api/

required:

 * **lang**: language code (`en`, `fr`, ...)

#### Returns

```json
{
  "source-generated": "iso-date",
  "resources": [
    {
      "name": "policies",
      "uri": "/api/policies/"
    },
    {
      "name": "activities",
      "uri": "/api/activities/"
    }
  ]
}
```

### GET /api/policies/

required:

 * **lang**: language code

####Returns

```json
[
  {
    "code": "number (0-7)",
    "name": "string",
  },
  ...
]
```


### GET /api/activities/

#### Params

required:

 * **lang**: language code like `en`, `fr`, etc.

filters:

 * **policy**: iati_code
 * **country**: iati_code

#### Returns

```json
[
  {
    "uri": "uri",
    "start": "iso date",
    "end": "iso date",
    "policy": "code name",
    "country": "country name",
    "organization": "name"
  },
  .
  .
  .
]

```

### GET /api/activities/&lt;iati_code&gt;

#### Params

required

 * **lang**: language code like `en`, `fr`, etc.

#### Returns

```json
{
  "id": "unique id",
  "title": "string",
  "start": "iso date",
  "end": "iso date",
  "policy": [
    {
      "iati_code": "code",
      "name": "string",
      "significance": "int (0 - 3; not significant - exclusive focus)"
    },
    ...
  ],
  "country": "name",
  "organization": "name",
  "description": "description",
  "result": "result description"
}
```

