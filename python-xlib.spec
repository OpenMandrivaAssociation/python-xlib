Summary: Python bindings to xlib
Name: python-xlib
Version: 0.23
Release: 1
Url: https://github.com/python-xlib/python-xlib
Source0: https://github.com/python-xlib/python-xlib/releases/download/0.23/python-xlib-0.23.tar.bz2
License: LGPLv2.1+
Group: Development/Python
BuildRequires: pkgconfig(python3)
BuildRequires: python3dist(setuptools)
BuildArch: noarch

%description
Python bindings to xlib

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
