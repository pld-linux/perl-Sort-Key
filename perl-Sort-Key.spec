#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Sort
%define		pnam	Key
Summary:	Sort::Key - interface to sort arrays by one or manipulate calculated keys
Summary(pl.UTF-8):	Sort::Key - interfejs do szybkiego sortowania tablic według zmiennych kluczy
Name:		perl-Sort-Key
Version:	1.33
Release:	4
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sort/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a37ab0da0cfdc26e57b4c79e39f6d98f
URL:		https://metacpan.org/dist/Sort-Key
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort arrays by one or multiple calculated keys.

%description -l pl.UTF-8
Sortowanie tablic po jednym lub wielu wyliczanych kluczach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Sort/Key.pm
%dir %{perl_vendorarch}/Sort
%{perl_vendorarch}/Sort/Key
%dir %{perl_vendorarch}/auto/Sort
%dir %{perl_vendorarch}/auto/Sort/Key
%attr(755,root,root) %{perl_vendorarch}/auto/Sort/Key/Key.so
%{_mandir}/man3/Sort::Key*.3pm*
