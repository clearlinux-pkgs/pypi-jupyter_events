#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_events
Version  : 0.6.3
Release  : 6
URL      : https://files.pythonhosted.org/packages/d0/b0/7afcd1d66834f43d08ec47c861a5540d7ad57eab47605ccd83429c147755/jupyter_events-0.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/b0/7afcd1d66834f43d08ec47c861a5540d7ad57eab47605ccd83429c147755/jupyter_events-0.6.3.tar.gz
Summary  : Jupyter Event System library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_events-bin = %{version}-%{release}
Requires: pypi-jupyter_events-license = %{version}-%{release}
Requires: pypi-jupyter_events-python = %{version}-%{release}
Requires: pypi-jupyter_events-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Jupyter Events
[![Build Status](https://github.com/jupyter/jupyter_events/actions/workflows/python-tests.yml/badge.svg?query=branch%3Amain++)](https://github.com/jupyter/jupyter_events/actions/workflows/python-tests.yml/badge.svg?query=branch%3Amain++)
[![codecov](https://codecov.io/gh/jupyter/jupyter_events/branch/main/graph/badge.svg?token=S9WiBg2iL0)](https://codecov.io/gh/jupyter/jupyter_events)
[![Documentation Status](https://readthedocs.org/projects/jupyter-events/badge/?version=latest)](http://jupyter-events.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the pypi-jupyter_events package.
Group: Binaries
Requires: pypi-jupyter_events-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_events package.


%package license
Summary: license components for the pypi-jupyter_events package.
Group: Default

%description license
license components for the pypi-jupyter_events package.


%package python
Summary: python components for the pypi-jupyter_events package.
Group: Default
Requires: pypi-jupyter_events-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_events package.


%package python3
Summary: python3 components for the pypi-jupyter_events package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_events)
Requires: pypi(jsonschema)
Requires: pypi(python_json_logger)
Requires: pypi(pyyaml)
Requires: pypi(rfc3339_validator)
Requires: pypi(rfc3986_validator)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-jupyter_events package.


%prep
%setup -q -n jupyter_events-0.6.3
cd %{_builddir}/jupyter_events-0.6.3
pushd ..
cp -a jupyter_events-0.6.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673626062
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_events
cp %{_builddir}/jupyter_events-%{version}/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-jupyter_events/45de8fc6727f3756d350b6f84a8f31ed2266af5c || :
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
/usr/bin/jupyter-events

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_events/45de8fc6727f3756d350b6f84a8f31ed2266af5c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
