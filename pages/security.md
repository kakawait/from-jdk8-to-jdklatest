---
layout: section-title
image: /images/security.png
---

# Security


---
layout: feature
title: General 1/3
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK17', jep: '415', text: 'Validate Incoming Serialization Data.' },
    { jdk: 'JDK15', jep: '339', text: 'Edwards-Curve Digital Signature Algorithm (EdDSA).' },
    { jdk: 'JDK11', jep: '332', text: 'TLS 1.3 support.' },
    { jdk: 'JDK11', jep: '324', text: 'Key Agreement with Curve25519 and Curve448.' },
    { jdk: 'JDK11', jep: '329', text: 'ChaCha20 and Poly1305 Cryptographic Algorithms.' },
    { jdk: 'JDK10', jep: '319', text: 'Default set of root Certification Authority (CA) certificates are provided with the JDK, so TLS connections are working out of the box.' },
    { jdk: 'JDK9', jep: '229', text: 'Default keystore type is the standard PKCS12 instead of the proprietary JKS.' },
    { jdk: 'JDK9', jep: '273', text: 'DRBG-Based SecureRandom.' },
    { jdk: 'JDK9', text: 'Disable X.509 certificate chains with SHA-1 based signatures.' },
    { jdk: 'JDK9', jep: '287', text: 'SHA-3 Hash Algorithms.' },
  ]"
/>

---
layout: feature
title: General 2/3
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK25', jep: '470', preview: true, text: 'PEM Encodings (native support for reading and writing PEM cryptographic formats).' },
    { jdk: 'JDK25', jep: '510', text: 'Key Derivation Function API (KDF) for modern security protocols like HKDF-SHA256.' },
    { jdk: 'JDK24', jep: '486', text: 'Remove the Security Manager.' },
    { jdk: 'JDK24', jep: '496, 497', text: 'Quantum-Resistant Cryptography (ML-KEM and ML-DSA) to protect against future quantum computing attacks.' },
    { jdk: 'JDK22', text: 'Use java <code>-XshowSettings:security</code> to view the security-related configuration information of the JVM.' },
    { jdk: 'JDK21', text: 'Support for Leighton-Micali Signature (LMS) signature verification and PBES2 cryptographic algorithms.' },
    { jdk: 'JDK21', jep: '452', text: 'Key Encapsulation Mechanism (KEM) API, a cryptographic technique for securing symmetric keys using public-key cryptography.' },
    { jdk: 'JDK18', text: 'The cacerts keystore file is now a passwordless PKCS12 file.' },
    { jdk: 'JDK18', text: 'Calling keyStore.store(outputStream, null) on a PKCS12 KeyStore creates a passwordless PKCS12 file.' },
  ]"
/>

---
layout: feature
title: General 3/3
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK26', jep: '517', text: 'HTTP/3 Support in HttpClient providing default encryption via QUIC protocol.' },
  ]"
/>
