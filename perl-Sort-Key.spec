#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Key
Summary:	Sort::Key - interface to sort arrays by one or manipulate calculated keys
Summary(pl.UTF-8):	Sort::Key - interfejs do szybkiego sortowania tablic według zmiennych kluczy
Name:		perl-Sort-Key
Version:	1.28
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sort/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec9d003d68784a5643815c65124aad18
URL:		http://search.cpan.org/dist/Sort-Key/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%doc README Changes
%{perl_vendorarch}/Sort/*.pm
%dir %{perl_vendorarch}/Sort
%dir %{perl_vendorarch}/Sort/Key
%{perl_vendorarch}/Sort/Key/*
%dir %{perl_vendorarch}/auto/Sort
%dir %{perl_vendorarch}/auto/Sort/Key
%attr(755,root,root) %{perl_vendorarch}/auto/Sort/Key/*.so
%{_mandir}/man3/*
