#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cookiecutter
Version  : 1.7.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/58/f5/6f41fa38e6efe4a0e85771f99a4ad8c33b4c14f03b4cc53b459aac4a629a/cookiecutter-1.7.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/f5/6f41fa38e6efe4a0e85771f99a4ad8c33b4c14f03b4cc53b459aac4a629a/cookiecutter-1.7.3.tar.gz
Summary  : A command-line utility that creates projects from project templates, e.g. creating a Python package project from a Python package project template.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cookiecutter-bin = %{version}-%{release}
Requires: pypi-cookiecutter-license = %{version}-%{release}
Requires: pypi-cookiecutter-python = %{version}-%{release}
Requires: pypi-cookiecutter-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: cookiecutter
Provides: cookiecutter-python
Provides: cookiecutter-python3
BuildRequires : pypi(binaryornot)
BuildRequires : pypi(click)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jinja2_time)
BuildRequires : pypi(poyo)
BuildRequires : pypi(python_slugify)
BuildRequires : pypi(requests)
BuildRequires : pypi(six)

%description
# Cookiecutter
[![pypi](https://img.shields.io/pypi/v/cookiecutter.svg)](https://pypi.python.org/pypi/cookiecutter)
[![python](https://img.shields.io/pypi/pyversions/cookiecutter.svg)](https://pypi.python.org/pypi/cookiecutter)
[![Build Status](https://travis-ci.org/cookiecutter/cookiecutter.svg?branch=master)](https://travis-ci.org/cookiecutter/cookiecutter)
[![codecov](https://codecov.io/gh/cookiecutter/cookiecutter/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/cookiecutter/cookiecutter?branch=master)
[![slack](https://img.shields.io/badge/cookiecutter-Join%20on%20Slack-green?style=flat&logo=slack)](https://join.slack.com/t/cookie-cutter/shared_invite/enQtNzI0Mzg5NjE5Nzk5LTRlYWI2YTZhYmQ4YmU1Y2Q2NmE1ZjkwOGM0NDQyNTIwY2M4ZTgyNDVkNjMxMDdhZGI5ZGE5YmJjM2M3ODJlY2U)
[![docs](https://readthedocs.org/projects/cookiecutter/badge/?version=latest)](https://readthedocs.org/projects/cookiecutter/?badge=latest)
[![Code Qaulity](https://img.shields.io/scrutinizer/g/cookiecutter/cookiecutter.svg)](https://scrutinizer-ci.com/g/cookiecutter/cookiecutter/?branch=master)

%package bin
Summary: bin components for the pypi-cookiecutter package.
Group: Binaries
Requires: pypi-cookiecutter-license = %{version}-%{release}

%description bin
bin components for the pypi-cookiecutter package.


%package license
Summary: license components for the pypi-cookiecutter package.
Group: Default

%description license
license components for the pypi-cookiecutter package.


%package python
Summary: python components for the pypi-cookiecutter package.
Group: Default
Requires: pypi-cookiecutter-python3 = %{version}-%{release}

%description python
python components for the pypi-cookiecutter package.


%package python3
Summary: python3 components for the pypi-cookiecutter package.
Group: Default
Requires: python3-core
Provides: pypi(cookiecutter)
Requires: pypi(binaryornot)
Requires: pypi(click)
Requires: pypi(jinja2)
Requires: pypi(jinja2_time)
Requires: pypi(poyo)
Requires: pypi(python_slugify)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the pypi-cookiecutter package.


%prep
%setup -q -n cookiecutter-1.7.3
cd %{_builddir}/cookiecutter-1.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641424984
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cookiecutter
cp %{_builddir}/cookiecutter-1.7.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cookiecutter/7737442329e4672f2b2fcf8e63467704a2223610
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cookiecutter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cookiecutter/7737442329e4672f2b2fcf8e63467704a2223610

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
