# JDK

The JDK (Java Development Kit) is the full-featured development and runtime environment for Java, bundling the Java compiler (javac), a comprehensive set of development tools (such as javadoc, jdb, jar, etc.), and the JRE (Java Runtime Environment), which contains the JVM, core classes, and supporting files required to execute Java applications. While the JRE is solely intended for end-users running Java applications and omits developer tools, the JDK enables both compilation and execution, making it essential for development workflows. Since Java 9, the standalone JRE is no longer offered separately, and modularization via JPMS allows developers to create custom, minimized runtimes using tools like jlink. In practice, the JDK now serves as the default distribution for both development and production, while the historical distinction between JDK and JRE is largely obsolete except in legacy contexts.

## Tool overview

Some tools in the JDK with a simple example:

| Tool          | Purpose                                 | Example Command                                                                             |
| ------------- | --------------------------------------- | ------------------------------------------------------------------------------------------- |
| **javac**     | Compile Java source code                | `javac HelloWorld.java`                                                                     |
| **java**      | Run Java programs                       | `java HelloWorld`                                                                           |
| **jar**       | Package/distribute Java applications    | `jar cf app.jar *.class`                                                                    |
| **javadoc**   | Generate API documentation              | `javadoc -d doc HelloWorld.java`                                                            |
| **jdb**       | Debug Java applications                 | `jdb HelloWorld`                                                                            |
| **jconsole**  | Monitor/manage Java apps (GUI)          | `jconsole`                                                                                  |
| **jvisualvm** | Visual profiling/monitoring (GUI)       | `jvisualvm`                                                                                 |
| **jstack**    | View thread stack traces                | `jstack <pid>`                                                                              |
| **jmap**      | Memory stats/heap dumps                 | `jmap -heap <pid>`                                                                          |
| **jstat**     | JVM stats (GC, class loading, etc.)     | `jstat -gc <pid>`                                                                           |
| **jps**       | List Java processes                     | `jps`                                                                                       |
| **jinfo**     | JVM configuration info                  | `jinfo <pid>`                                                                               |
| **jshell**    | Interactive Java shell (REPL)           | `jshell`                                                                                    |
| **javap**     | Disassemble class files                 | `javap HelloWorld`                                                                          |
| **keytool**   | Manage keys/certificates/keystores      | `keytool -genkeypair -alias mykey -keystore mykeystore.jks`                                 |
| **serialver** | Show serialVersionUID for classes       | `serialver HelloWorld`                                                                      |
| **jlink**     | Custom runtime image creation (Java 9+) | `jlink --module-path mods --add-modules com.example.helloworld --output helloworld-runtime` |

## Comparing builds

| Name              | License                      | Supported By       | Open Source | Free  | LTS | Target Audience/Notes                       |
| ----------------- | ---------------------------- | ------------------ | ----------- | ----- | --- | ------------------------------------------- |
| Oracle JDK        | NFTC (Java 17+), earlier BCL | Oracle             | No          | Yes   | Yes | Official JDK, enterprise support            |
| OpenJDK           | GPLv2 + Classpath            | Community          | Yes         | Yes   | Yes | Upstream, most other JDKs are based on this |
| Amazon Corretto   | GPLv2 + Classpath            | Amazon             | Yes         | Yes   | Yes | Free, supported by AWS, LTS                 |
| Microsoft OpenJDK | MIT (binaries), GPLv2 (src)  | Microsoft          | Yes         | Yes   | Yes | For Azure, free, open source                |
| Eclipse Temurin   | GPLv2 + Classpath            | Eclipse Foundation | Yes         | Yes   | Yes | Broad adoption, successor to AdoptOpenJDK   |
| Red Hat OpenJDK   | GPLv2 + Classpath            | Red Hat            | Yes         | Yes   | Yes | Default for RHEL, commercial support        |
| Azul Zulu OpenJDK | GPLv2 + Classpath            | Azul Systems       | Yes         | Yes   | Yes | Commercial/enterprise options               |
| SAP SapMachine    | GPLv2 + Classpath            | SAP                | Yes         | Yes   | Yes | For SAP users                               |

## keytool

Keytool is a command-line utility that comes with the Java Development Kit (JDK). It is used to generate, import, export, and store keys and certificates.

Here are some more details on how to use it:

### Creation and Importing

Generate a Java keystore and key pair:

```bash
keytool -genkeypair -keyalg RSA -keysize 2048 -keystore keystore.jks -alias server -validity 3650
```

Generate a Java keystore and key pair with Distinguished Name and extensions:

```bash
keytool -genkeypair -keyalg RSA -keysize 2048 -keystore keystore.jks -alias server \
  -dname "CN=0xfab1,OU=net,O=lol,C=DE" -storepass secret -keypass secret -validity 3650 \
  -ext KeyUsage=digitalSignature,dataEncipherment,keyEncipherment,keyAgreement \
  -ext ExtendedKeyUsage=serverAuth,clientAuth \
  -ext SubjectAlternativeName=DNS:localhost,IP:127.0.0.1
```

Import a certificate into a Java keystore:

```bash
keytool -importcert -file server.crt -keystore truststore.jks -alias server
```

Generate a Root CA with signing capabilities:

```bash
keytool -genkeypair -keystore root-ca.jks -storepass secret -keypass secret -keyalg RSA -keysize 2048 \
  -alias root-ca -validity 3650 -dname "CN=Root-CA,OU=Certificate Authority,O=lol,C=DE" \
  -ext KeyUsage=digitalSignature,keyCertSign -ext BasicConstraints=ca:true,pathlen:3
```

Generate a Certificate Signing Request (CSR):

```bash
keytool -certreq -keystore keystore.jks -alias server -file server.csr
```

Import a root or intermediate CA certificate into a Java keystore:

```bash
keytool -import -trustcacerts -file root-ca.crt -alias my-newly-trusted-ca -keystore keystore.jks
```

Import keystore contents into another keystore:

```bash
keytool -importkeystore -srckeystore source.p12 -srcstoretype PKCS12 -srcstorepass changeit \
  -destkeystore target.p12 -deststoretype PKCS12 -deststorepass changeit
```

### Checking

Check a standalone certificate:

```bash
keytool -printcert -file server.crt
```

Check a standalone certificate in PEM format:

```bash
keytool -printcert -file server.crt -rfc
```

List certificates in a keystore:

```bash
keytool -list -v -keystore keystore.jks
```

List details of a specific keystore entry:

```bash
keytool -list -v -keystore keystore.jks -alias server
```

### Other Commands

Delete a certificate from a keystore:

```bash
keytool -delete -alias server -keystore keystore.jks
```

Change keystore password:

```bash
keytool -storepasswd -keystore keystore.jks
```

Change password of a key entry (only for JKS keystore):

```bash
keytool -keypasswd -alias server -keystore keystore.jks
```

Sign a CSR with a CA keystore:

```bash
keytool -gencert -infile server.csr -outfile server-signed.cer -keystore root-ca.jks \
  -storepass secret -alias root-ca -validity 3650 \
  -ext KeyUsage=digitalSignature,dataEncipherment,keyEncipherment,keyAgreement \
  -ext ExtendedKeyUsage=serverAuth,clientAuth
```

Sign a CSR with extensions for Subject Alternative Name and Authority Info Access:

```bash
keytool -gencert -infile server.csr -outfile server-signed.cer -keystore root-ca.jks \
  -storepass secret -alias root-ca -validity 3650 \
  -ext KeyUsage=digitalSignature,dataEncipherment,keyEncipherment,keyAgreement \
  -ext ExtendedKeyUsage=serverAuth,clientAuth \
  -ext SubjectAlternativeName=DNS:localhost,DNS:myserver.local,IP:127.0.0.1 \
  -ext AuthorityInfoAccess=caIssuers:uri:http://cacerts.digicert.com/DigiCertTLSRSASHA2562020CA1-1.crt
```

Convert JKS to PKCS12:

```bash
keytool -importkeystore -srckeystore keystore.jks -srcstoretype JKS -destkeystore keystore.p12 \
  -deststoretype PKCS12 -srcstorepass password -deststorepass password
```

Convert PKCS12 to JKS:

```bash
keytool -importkeystore -srckeystore keystore.p12 -srcstoretype PKCS12 -destkeystore keystore.jks \
  -deststoretype JKS -srcstorepass password -deststorepass password
```

### Exporting

Export a certificate in binary format:

```bash
keytool -exportcert -keystore keystore.jks -alias server -file server.crt
```

Export a certificate in PEM format:

```bash
keytool -exportcert -keystore keystore.jks -alias server -rfc -file server.crt
```

Export Java keystore to PKCS12 (.p12):

```bash
keytool -importkeystore -srckeystore keystore.jks -destkeystore keystore.p12 -srcstoretype JKS -deststoretype PKCS12
```
