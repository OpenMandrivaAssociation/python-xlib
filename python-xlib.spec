%define name python-xlib
%define version 0.14
%define release %mkrel 1

Summary: X11R6 client-side implementation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/python-xlib/%{name}-%{version}.tar.gz
Patch1: python-xlib-0.14-buffsize.patch
License: GPL
Group: Development/Python
Url: http://python-xlib.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildArch: noarch

%description
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

%prep
%setup -q
%patch1 -p1 -b .buffsize

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %attr(644,root,root) NEWS PKG-INFO README TODO
%{py_puresitedir}/Xlib
%{py_puresitedir}/*.egg-info


