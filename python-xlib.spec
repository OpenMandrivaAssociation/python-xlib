%define oname python_xlib

Name:	python-xlib
Version:	0.33
Release:	2
License:	LGPLv2.1+
Summary:	Python bindings to xlib
Group:		Development/Python
URL:		https://github.com/python-xlib/python-xlib
Source0:	https://github.com/python-xlib/python-xlib/releases/download/%{version}/python-xlib-%{version}.tar.bz2
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python)
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
