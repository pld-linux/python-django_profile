%define		module		profile
%define		svnrev		r420
Summary:	Django pluggable user profile zone
Name:		python-django_profile
Version:	0.6
Release:	1.%{svnrev}.0.1
License:	MIT
Group:		Development/Languages/Python
#Source0:	http://django-profile.googlecode.com/files/django-%{module}-%{version}.tgz
Source0:	django-profile-%{svnrev}.tgz
# Source0-md5:	c0d3893085535bed3389674c550436a5
URL:		http://code.google.com/p/django-profile/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-django >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Django pluggable user profile zone which can be used and
customized easily in your social application web platform developed in
django.

It's developed with Django for the backend framework and uses Jquery
as the javascript library for the client UI. It avoids big amounts of
development time process in such a generic thing as the User Profile
and account utilities.

%prep
%setup -q -n django-profile

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/demo
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/userprofile-0.6-py2.6.egg-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/userprofile
