%define prever rc1

Summary: X11R6 client-side implementation
Name: python-xlib
Version: 0.15
Release: %mkrel -c %{prever} 1
Source0: http://downloads.sourceforge.net/python-xlib/%{name}-%{version}%{?prever}.tar.bz2
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
%setup -q -n %{name}-%{version}%{?prever}
%patch1 -p1 -b .buffsize
chmod -R a+r .

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README TODO
%{py_puresitedir}/Xlib
%{py_puresitedir}/*.egg-info




%changelog
* Mon Apr 12 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.15-0.rc1.1mdv2010.1
+ Revision: 533710
- new release candidate version 0.15rc1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.14-5mdv2010.0
+ Revision: 442547
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.14-4mdv2009.1
+ Revision: 320353
- rebuild for new python

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.14-3mdv2009.0
+ Revision: 269045
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 28 2008 Olivier Blin <oblin@mandriva.com> 0.14-2mdv2009.0
+ Revision: 198856
- fix doc directory permissions (by making all source files readable and removing wrong attrs)

* Sun Mar 02 2008 Olivier Blin <oblin@mandriva.com> 0.14-1mdv2008.1
+ Revision: 177732
- PKG-INFO has been removed
- rediff buffer size patch
- remove merged Xauth patch
- 0.14

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.13-2mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 30 2006 Olivier Blin <oblin@mandriva.com> 0.13-2mdv2007.0
+ Revision: 102795
- enlarge socket buffer size
- use slices instead of buffer() calls to build unpack() arguments (fix Xauthority parsing)

* Fri Dec 29 2006 Olivier Blin <oblin@mandriva.com> 0.13-1mdv2007.1
+ Revision: 102540
- buildrequires python-devel
- fix doc permissions
- initial python-xlib release
- Create python-xlib

