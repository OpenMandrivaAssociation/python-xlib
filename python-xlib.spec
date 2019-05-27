Summary: Python bindings to xlib
Name: python-xlib
Version: 0.25
Release: 1
Url: https://github.com/python-xlib/python-xlib
Source0: https://github.com/python-xlib/python-xlib/releases/download/%{version}/python-xlib-%{version}.tar.bz2
License: LGPLv2.1+
Group: Development/Python
BuildRequires: pkgconfig(python3)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildArch: noarch

%description
Python bindings to xlib.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%defattr(-,root,root)
%{py_puresitedir}/Xlib
%{py_puresitedir}/*.egg-info
