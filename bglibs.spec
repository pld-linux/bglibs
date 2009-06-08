Summary:	Bruce Guenter's Libraries Collection
Summary(pl.UTF-8):	Zestaw bibliotek Bruce'a Guentera
Name:		bglibs
Version:	1.106
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://untroubled.org/bglibs/%{name}-%{version}.tar.gz
# Source0-md5:	99bf5936456c7661c329beab63d2b520
URL:		http://untroubled.org/bglibs/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bruce Guenter's Libraries Collection.

%description -l pl.UTF-8
Zestaw bibliotek Bruce'a Guentera.

%package devel
Summary:	bglibs header files
Summary(pl.UTF-8):	Pliki nagłówkowe bglibs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for bglibs.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla bglibs.

%package static
Summary:	Static version of bglibs
Summary(pl.UTF-8):	Statyczne wersje bglibs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of bglibs with shared equivalents.

%description static -l pl.UTF-8
Statyczne wersje bglibs mających odpowiedniki współdzielone.

%prep
%setup -q

%build
echo '%{__cc} %{rpmcflags} -Wall' > conf-cc
echo '%{__cc} %{rpmldflags}' > conf-ld
echo '%{_prefix}' > conf-home
echo "%{_bindir}" > conf-bin
echo "%{_mandir}" > conf-man
echo "%{_includedir}/%{name}" > conf-include
echo "%{_libdir}/%{name}" > conf-lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

echo "$RPM_BUILD_ROOT%{_prefix}" > conf-home
echo "$RPM_BUILD_ROOT%{_bindir}" > conf-bin
echo "$RPM_BUILD_ROOT%{_mandir}" > conf-man
echo "$RPM_BUILD_ROOT%{_includedir}/%{name}" > conf-include
echo "$RPM_BUILD_ROOT%{_libdir}/%{name}" > conf-lib

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libbg.so.*
%attr(755,root,root) %{_libdir}/%{name}/libbg-sysdeps.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bg-installer
%attr(755,root,root) %{_bindir}/cli-generate
%attr(755,root,root) %{_bindir}/crc-gentab
%attr(755,root,root) %{_libdir}/%{name}/libbg.so
%attr(755,root,root) %{_libdir}/%{name}/libbg-sysdeps.so
%{_libdir}/%{name}/libbg.la
%{_libdir}/%{name}/libbg-sysdeps.la
# static-only
%{_libdir}/%{name}/libbg-adt.a
%{_libdir}/%{name}/libbg-base64.a
%{_libdir}/%{name}/libbg-cdb.a
%{_libdir}/%{name}/libbg-cli.a
%{_libdir}/%{name}/libbg-crc.a
%{_libdir}/%{name}/libbg-crypto.a
%{_libdir}/%{name}/libbg-dict.a
%{_libdir}/%{name}/libbg-fmt.a
%{_libdir}/%{name}/libbg-installer.a
%{_libdir}/%{name}/libbg-instcheck.a
%{_libdir}/%{name}/libbg-instshow.a
%{_libdir}/%{name}/libbg-iobuf.a
%{_libdir}/%{name}/libbg-misc.a
%{_libdir}/%{name}/libbg-msg.a
%{_libdir}/%{name}/libbg-net.a
%{_libdir}/%{name}/libbg-path.a
%{_libdir}/%{name}/libbg-str.a
%{_libdir}/%{name}/libbg-unix.a
%{_libdir}/%{name}/libpwcmp-module.a
%{_libdir}/%{name}/libpwcmp.a
%{_libdir}/%{name}/libvmailmgr.a
# symlinks
%{_libdir}/%{name}/libinstaller.a
%{_libdir}/%{name}/libinstcheck.a
%{_libdir}/%{name}/libinstshow.a
# dirs with symlinks to libbg-*.a
%{_libdir}/%{name}/base64
%{_libdir}/%{name}/cdb
%{_libdir}/%{name}/cli
%{_libdir}/%{name}/crypto
%{_libdir}/%{name}/dict
%{_libdir}/%{name}/iobuf
%{_libdir}/%{name}/misc
%{_libdir}/%{name}/msg
%{_libdir}/%{name}/net
%{_libdir}/%{name}/path
%{_libdir}/%{name}/pwcmp
%{_libdir}/%{name}/str
%{_libdir}/%{name}/unix
%{_libdir}/%{name}/vmailmgr
# linking "scripts"
%{_libdir}/%{name}/crypt.lib
%{_libdir}/%{name}/dl.lib
%{_libdir}/%{name}/m.lib
%{_libdir}/%{name}/net.lib
%{_libdir}/%{name}/rt.lib
%{_libdir}/%{name}/s.lib
%{_libdir}/%{name}/shadow.lib
%{_libdir}/%{name}/socket.lib
%{_includedir}/%{name}
%{_mandir}/man1/cli-generate.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}/libbg.a
%{_libdir}/%{name}/libbg-sysdeps.a
# symlinks
%{_libdir}/%{name}/libsysdeps.a
