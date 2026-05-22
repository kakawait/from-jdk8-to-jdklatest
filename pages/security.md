---
layout: section-title
image: /images/security.png
---

# Security


---
layout: feature
title: General 1/2
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK11', text: 'TLS 1.3 support.' },
    { jdk: 'JDK11', text: 'Key Agreement with Curve25519 and Curve448.' },
    { jdk: 'JDK11', text: 'ChaCha20 and Poly1305 Cryptographic Algorithms.' },
    { jdk: 'JDK10', text: 'Default set of root Certification Authority (CA) certificates are provided with the JDK, so TLS connections are working out of the box.' },
    { jdk: 'JDK9', text: 'Default keystore type is the standard PKCS12 instead of the proprietary JKS.' },
    { jdk: 'JDK9', text: 'DRBG-Based SecureRandom.' },
    { jdk: 'JDK9', text: 'Disable X.509 certificate chains with SHA-1 based signatures.' },
    { jdk: 'JDK9', text: 'SHA-3 Hash Algorithms.' },
  ]"
/>

---
layout: feature
title: General 2/2
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK22', text: 'Use java <code>-XshowSettings:security</code> to view the security-related configuration information of the JVM.' },
    { jdk: 'JDK21', text: 'Support for Leighton-Micali Signature (LMS) signature verification and PBES2 cryptographic algorithms.' },
    { jdk: 'JDK21', text: 'Key Encapsulation Mechanism (KEM) API, a cryptographic technique for securing symmetric keys using public-key cryptography.' },
    { jdk: 'JDK18', text: 'The cacerts keystore file is now a passwordless PKCS12 file.' },
    { jdk: 'JDK18', text: 'Calling keyStore.store(outputStream, null) on a PKCS12 KeyStore creates a passwordless PKCS12 file.' },
    { jdk: 'JDK17', text: 'Validate Incoming Serialization Data.' },
    { jdk: 'JDK15', text: 'Edwards-Curve Digital Signature Algorithm (EdDSA).' },
  ]"
/>
