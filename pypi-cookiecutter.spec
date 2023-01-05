#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cookiecutter
Version  : 2.1.1
Release  : 23
URL      : https://files.pythonhosted.org/packages/96/43/65a3dad94dceaaaa12807ce4d4eff1064db6e91a8c6fb6945e3e61e63552/cookiecutter-2.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/96/43/65a3dad94dceaaaa12807ce4d4eff1064db6e91a8c6fb6945e3e61e63552/cookiecutter-2.1.1.tar.gz
Summary  : A command-line utility that creates projects from project templates, e.g. creating a Python package project from a Python package project template.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cookiecutter-bin = %{version}-%{release}
Requires: pypi-cookiecutter-license = %{version}-%{release}
Requires: pypi-cookiecutter-python = %{version}-%{release}
Requires: pypi-cookiecutter-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(binaryornot)
BuildRequires : pypi(click)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jinja2_time)
BuildRequires : pypi(python_slugify)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Cookiecutter
[![pypi](https://img.shields.io/pypi/v/cookiecutter.svg)](https://pypi.org/project/cookiecutter/)
[![python](https://img.shields.io/pypi/pyversions/cookiecutter.svg)](https://pypi.org/project/cookiecutter/)
[![Build Status](https://github.com/cookiecutter/cookiecutter/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/cookiecutter/cookiecutter/actions)
[![codecov](https://codecov.io/gh/cookiecutter/cookiecutter/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/cookiecutter/cookiecutter?branch=master)
[![discord](https://img.shields.io/badge/Discord-cookiecutter-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/9BrxzPKuEW)
[![docs](https://readthedocs.org/projects/cookiecutter/badge/?version=latest)](https://readthedocs.org/projects/cookiecutter/?badge=latest)
[![Code Quality](https://img.shields.io/scrutinizer/g/cookiecutter/cookiecutter.svg)](https://scrutinizer-ci.com/g/cookiecutter/cookiecutter/?branch=master)

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
Requires: pypi(python_slugify)
Requires: pypi(pyyaml)
Requires: pypi(requests)

%description python3
python3 components for the pypi-cookiecutter package.


%prep
%setup -q -n cookiecutter-2.1.1
cd %{_builddir}/cookiecutter-2.1.1
pushd ..
cp -a cookiecutter-2.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672265125
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cookiecutter
cp %{_builddir}/cookiecutter-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cookiecutter/03460e483288718db7878b66bd90ab06e7346469 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cookiecutter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cookiecutter/03460e483288718db7878b66bd90ab06e7346469

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
