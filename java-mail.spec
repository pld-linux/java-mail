#
# Conditional build:
%bcond_without  javadoc         # don't build javadoc

%define		srcname	mail
%define		ver		%(echo %{version} | tr . _)
Summary:	JavaMail - Java mail system
Summary(pl.UTF-8):	JavaMail - system pocztowy w Javie
Name:		java-mail
Version:	1.4.4
Release:	1
License:	CDDL
Group:		Libraries/Java
#Source0:	http://download.oracle.com/otn-pub/java/javamail/%{version}/javamail%{ver}.zip
Source0:	http://download.java.net/maven/2/com/sun/mail/javax.mail/%{version}/javax.mail-%{version}-sources.jar
# Source0-md5:	605fd51ed38eb2af777d40fc29454008
URL:		http://www.oracle.com/technetwork/java/javamail/index.html
BuildRequires:	java(jaf)
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java(jaf)
Requires:	jpackage-utils
Provides:	java(javamail) = %{version}-%{release}
Obsoletes:	java(javamail)
Obsoletes:	javamail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The JavaMail(TM) API provides a set of abstract classes that model a
mail system. The API provides a platform independent and protocol
independent framework to build Java technology-based mail and
messaging applications.

%description -l pl.UTF-8
API JavaMail(TM) daje zestaw klas abstrakcyjnych tworzących system
pocztowy. API daje niezależne od platformy i protokołu środowisko do
tworzenia aplikacji pocztowych i komunikacyjnych w oparciu o Javę.

%package javadoc
Summary:	Online manual for java-mail
Summary(pl.UTF-8):	Dokumentacja online do java-mail
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	javamail-doc

%description javadoc
Documentation for java-mail.

%description javadoc -l pl.UTF-8
Dokumentacja do java-mail.

%description javadoc -l fr.UTF-8
Javadoc pour java-mail.

%prep
%setup -qc

%build
CLASSPATH=$(build-classpath activation)

install -d build
%javac \
	-classpath $CLASSPATH \
	-source 1.4 \
	-target 1.4 \
	-d build $(find -name '*.java')

%jar \
	-cfm %{srcname}-%{version}.jar \
	META-INF/MANIFEST.MF \
	-C build \
	. META-INF

%if %{with javadoc}
%javadoc -d apidocs \
	$(find com/sun/mail -name '*.java')
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/javamail-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/javamail.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/%{srcname}.jar
%{_javadir}/javamail-%{version}.jar
%{_javadir}/javamail.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
