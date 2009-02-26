#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	FormFu
Summary:	HTML::FormFu - HTML Form Creation, Rendering and Validation Framework
#Summary(pl.UTF-8):	
Name:		perl-HTML-FormFu
Version:	0.03007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e29b491c3ed8a88139ab7ee2374e8334
URL:		http://www.formfu.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Captcha::reCAPTCHA) >= 0.92
BuildRequires:	perl(DateTime::Format::Builder) >= 0.7901
BuildRequires:	perl(DateTime::Format::Natural)
BuildRequires:	perl(DateTime::Format::Strptime)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(Regexp::Copy)
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Class-C3
BuildRequires:	perl-Config-Any >= 0.10
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-DES
BuildRequires:	perl-Data-Visitor
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-DateTime >= 0.38
BuildRequires:	perl-DateTime-Locale
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-HTML-Scrubber
BuildRequires:	perl-HTML-TokeParser-Simple >= 3.14
BuildRequires:	perl-libwww >= 1.64
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Readonly
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Template-Toolkit
BuildRequires:	perl-YAML-Syck >= 1.05
BuildRequires:	perl-Test-NoWarnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FormFu is a HTML form framework which aims to be as easy as 
possible to use for basic web forms, but with the power and flexibility
to do anything else you might want to do (as long as it involves forms).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/HTML/*.pm
%{perl_vendorlib}/HTML/FormFu
%{perl_vendorlib}/auto/share/dist/HTML-FormFu
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
