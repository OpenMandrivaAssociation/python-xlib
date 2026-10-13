%define oname python_xlib

Name:	python-xlib
Version:	0.33
Release:	3
License:	LGPLv2.1+
Summary:	Python bindings to xlib
Group:		Development/Python
URL:		https://github.com/python-xlib/python-xlib
Source0:	https://github.com/python-xlib/python-xlib/releases/download/%{version}/python-xlib-%{version}.tar.bz2
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	dos2unix

%description
Python bindings to xlib.

%prep
%autosetup -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info
# setuptools >= 82 removed pkg_resources. The import only checked setuptools>=30.
sed -i \
	-e '/pkg_resources/d' \
	-e '/setuptools_require/d' \
	-e '/assert setuptools_version/d' \
	-e '/Check setuptools is recent enough/d' \
	-e 's/from setuptools import (__version__ as setuptools_version, setup)/from setuptools import setup/' \
	setup.py
dos2unix CHANGELOG.md README.rst TODO dev-requirements.txt test/*

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/Xlib
%{python_sitelib}/%{oname}-%{version}*.*-info
