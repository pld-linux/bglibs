Summary:	Bruce Guenter's Libraries Collection
Summary(pl):	Zestaw bibliotek Bruce'a Guentera
Name:		bglibs
Version:	1.102
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://untroubled.org/bglibs/%{name}-%{version}.tar.gz
# Source0-md5:	0615125e33abe30ecd50e63bcd43aa72
URL:		http://untroubled.org/bglibs/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bruce Guenter's Libraries Collection.

%description -l pl
Zestaw bibliotek Bruce'a Guentera.

%package devel
Summary:	bglibs header files
Summary(pl):	Pliki nag³ówkowe bglibs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for bglibs.

%description devel -l pl
Pliki nag³ówkowe dla bglibs.

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
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
