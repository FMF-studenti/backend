# Študentske strani FMF - Django Backend
[![Homepage][web-img]][web] [![Latest release][release-img]][release] [![License][license-img]][license]

This is a Python3 and Django powered backend for FMF.si, student community of Faculty of Mathematics and Physics, University of Ljubljana.


## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Python 3](https://www.python.org)
* [MariaDB](https://mariadb.com) or another Django compatible database


## Installation

* `git clone https://github.com/FMF-studenti/backend.git`
* change into the new directory
* `virtualenv venv -p python3`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* copy `sample.env` to `.env` and adapt to your local environment
* migrate database `foreman run python manage.py migrate`
* (optional) create admin user `foreman run python manage.py createsuperuser`
* (optional) install [Discourse](http://discourse.org) for local integration development]
* (optional) install foreman for easier local running


## Running / Development

* always make sure you are in the correct virtualenv
  (`source venv/bin/activate`)
* `foreman start`
* visit the backend at [http://localhost:5000](http://localhost:5000)
* (optional) import fixtures: `foreman run python manage.py loaddata <file>`
* (optional) export variables in `.env` and run `manage.py` commands directly

### Running Tests

TODO

### Deploying

* follow installation steps and add uwsgi vassal with `uwsgi.ini`
* checkout latest tag/stable code on server
* `foreman run python manage.py collectstatic`
* restart `uwsgi-emperor` service


## Further Reading / Useful Links

* [Python 3](https://www.python.org)
* [Django](https://www.djangoproject.com)
* [Django REST Framework](http://www.django-rest-framework.org)


## Copyright
Copyright (C) 2015 Tadej Novak

This project may be used under the terms of the GNU General Public License
version 2.0 (or later) as published by the Free Software Foundation and
appearing in the file LICENSE.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the license for more details.


[web]: http://fmf.si
[release]: https://github.com/FMF-studenti/backend/releases
[license]: https://github.com/FMF-studenti/backend/blob/master/LICENSE

[web-img]: https://img.shields.io/badge/web-fmf.si-green.svg
[license-img]: https://img.shields.io/github/license/FMF-studenti/backend.svg
[release-img]: https://img.shields.io/github/release/FMF-studenti/backend.svg
