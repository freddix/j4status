Summary:	A plugin-based status line generator
Name:		j4status
Version:	20130216
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/sardemff7/j4status/archive/master.zip
# Source0-md5:	cfdc12fc0a1d220629ac518f7e4c2e87
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	upower-libs
BuildRequires:	yajl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -qn %{name}-master

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-sensors-input	\
	--disable-silent-rules	\
	--enable-systemd-input
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/j4status
%dir %attr(755,root,root) %{_libdir}/j4status
%dir %attr(755,root,root) %{_libdir}/j4status/plugins
%attr(755,root,root) %{_libdir}/j4status/plugins/file-monitor.so
%attr(755,root,root) %{_libdir}/j4status/plugins/flat.so
%attr(755,root,root) %{_libdir}/j4status/plugins/i3bar.so
%attr(755,root,root) %{_libdir}/j4status/plugins/nm.so
%attr(755,root,root) %{_libdir}/j4status/plugins/systemd.so
%attr(755,root,root) %{_libdir}/j4status/plugins/time.so
%attr(755,root,root) %{_libdir}/j4status/plugins/upower.so

%attr(755,root,root) %ghost %{_libdir}/libj4status-plugin.so.0
%attr(755,root,root) %{_libdir}/libj4status-plugin.so.*.*.*

%{_mandir}/man1/j4status.1*
%{_mandir}/man5/j4status-file-monitor.conf.5*
%{_mandir}/man5/j4status-i3bar.conf.5*
%{_mandir}/man5/j4status-nm.conf.5*
%{_mandir}/man5/j4status-systemd.conf.5*
%{_mandir}/man5/j4status-time.conf.5*
%{_mandir}/man5/j4status.conf.5*

