# comment
# - what about files (not included in %files in previous version):
#   /usr/lib/bglibs/bin/bg-installer
#   /usr/lib/bglibs/bin/crc-gentab

Summary:	Bruce Guenter's Libraries Collection
Summary(pl):	Zestaw bibliotek Bruce'a Guentera
Name:		bglibs
Version:	1.024
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://untroubled.org/bglibs/%{name}-%{version}.tar.gz
# Source0-md5:	34b04bc84538bf39fef53910b025188e
URL:		http://untroubled.org/bglibs/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# it cannot be installed in /usr/{include,lib} because of filename collisions
%define		_prefix		/usr/%{_lib}/bglibs

%description
Bruce Guenter's Libraries Collection.

%description -l pl
Zestaw bibliotek Bruce'a Guentera.

%prep
%setup -q

%build
echo '%{__cc} %{rpmcflags} -Wall' > conf-cc
echo '%{_prefix}' > conf-home
echo '%{__cc} %{rpmldflags}' > conf-ld

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

echo "$RPM_BUILD_ROOT%{_bindir}" > conf-bin
echo "$RPM_BUILD_ROOT%{_prefix}/include" > conf-include
echo "$RPM_BUILD_ROOT%{_prefix}/lib" > conf-lib

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%dir %{_prefix}
%{_prefix}/include
%{_prefix}/lib
