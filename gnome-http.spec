%define	snap	20010401
Summary:	GNOME - http library
Summary(pl):	GNOME - biblioteka http
Name:		gnome-http
Version:	0.1
Release:	0.%{snap}
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-http/%{name}-%{snap}.tar.gz
# Source0-md5: fae75251f240b7e4bef0c830b40fb0c5
URL:		http://www.gnome.org/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME http library.

%description -l pl
Biblioteka http GNOME.

%package devel
Summary:	gnome-http - header files
Summary(pl):	gnome-http - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains header files.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe.

%package static
Summary:	gnome-http - static libraries
Summary(pl):	gnome-http - biblioteki statyczne
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries.

%description static -l pl
Pakiet ten zawiera biblioteki statyczne.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
