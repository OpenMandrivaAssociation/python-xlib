Summary: Python bindings to xlib
Name: python-xlib
Version:	0.33
Release:	1
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
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%defattr(-,root,root)
%{py_puresitedir}/Xlib
%{py_puresitedir}/*.egg-info
