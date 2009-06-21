Summary:	Off-the-Record Messaging Library
#Summary(pl.UTF-8):
Name:		libotr
Version:	3.2.0
Release:	2
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
# Source0-md5:	faba02e60f64e492838929be2272f839
URL:		http://www.cypherpunks.ca/otr/
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the portable OTR Messaging Library, as well as the toolkit to
help you forge messages.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for OTR library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OTR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OTR library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OTR.

%package static
Summary:	Static OTR library
Summary(pl.UTF-8):	Statyczna biblioteka OTR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OTR library.

%description static -l pl.UTF-8
Statyczna biblioteka OTR.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/otr_*
%attr(755,root,root) %{_libdir}/libotr.so.2.2.0
%attr(755,root,root) %ghost %{_libdir}/libotr.so.2
%{_mandir}/man1/otr_*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libotr.so
%{_libdir}/libotr.la
%{_includedir}/libotr
%{_aclocaldir}/libotr.m4
%{_pkgconfigdir}/libotr.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libotr.a
