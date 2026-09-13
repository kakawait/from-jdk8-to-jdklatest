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
    { jdk: 'JDK27', jep: '527', text: 'Post-Quantum Hybrid Key Exchange for TLS 1.3, combining ML-KEM with classic ECDHE algorithms.' },
    { jdk: 'JDK27', jep: '536', text: 'JFR In-Process Data Redaction: secrets passed as JVM arguments, environment variables or system properties are masked in recordings.' },
    { jdk: 'JDK27', text: 'TLS certificate compression support.' },
    { jdk: 'JDK27', text: 'WISeKey certificates added to the JVM truststore.' },
    { jdk: 'JDK26', jep: '517', text: 'HTTP/3 Support in HttpClient providing default encryption via QUIC protocol.' },
  ]"
/>

---
layout: feature
title: Post-Quantum Hybrid Key Exchange for TLS 1.3
jep: '527'
---
<template #badge>
  <JdkVersions v="27" />
</template>

TLS 1.3 gains **hybrid key exchange**: a quantum-resistant algorithm combined with a traditional one, so the session remains secure as long as **one** of the two is not broken. It extends the ML-KEM support introduced by JEP 496 in JDK 24.

Three new hybrid schemes combine **ML-KEM** with **ECDHE**:

- `X25519MLKEM768` - ECDHE with X25519 + ML-KEM-768
- `SecP256r1MLKEM768` - ECDHE with secp256r1 + ML-KEM-768
- `SecP384r1MLKEM1024` - ECDHE with secp384r1 + ML-KEM-1024

<div class="mt-4 text-[13px] opacity-80">
This protects against "harvest now, decrypt later" attacks while acknowledging that the new algorithms have not benefited from as many years of analysis as the classical ones.
</div>

---
layout: feature
title: JFR In-Process Data Redaction
jep: '536'
---
<template #badge>
  <JdkVersions v="27" />
</template>

JFR recordings contain the command line, environment variables and system properties of the process, and therefore secrets that should not leak when a recording is shared. JDK 27 **masks them by default**, and lets you add your own filters: case-insensitive glob patterns where `*` and `?` are wildcards.

<JdkCodeBlock label="JDK27" color="#64748b" size="small" contentClass="text-[10.5px] leading-tight">

```bash
# Redact any key matching 'dburl' in addition to the default filters ('+' keeps them)
java -XX:FlightRecorderOptions:redact-key=+dburl \
     -XX:StartFlightRecording:filename=dump.jfr -jar app.jar

# Redact command-line arguments looking like a URL with credentials
java -XX:FlightRecorderOptions:redact-argument='https://*:*@*' \
     -XX:StartFlightRecording:filename=dump.jfr -jar app.jar

# Read many filters from a file, or drop the default filters entirely
java -XX:FlightRecorderOptions:redact-arguments=@args.txt \
     -XX:StartFlightRecording:filename=dump.jfr -jar app.jar
java -XX:FlightRecorderOptions:redact-key=none \
     -XX:StartFlightRecording:filename=dump.jfr -jar app.jar
```

</JdkCodeBlock>

<div class="mt-3 text-[12px] leading-snug opacity-80">
Default filters cover <code>*api*key*</code>, <code>*auth*</code>, <code>*client*secret*</code>, <code>*credential*</code>, <code>*passphrase*</code>, <code>*passwd*</code>, <code>*password*</code>, <code>*private*key*</code>, <code>*pwd*</code>, <code>*secret*</code> and <code>*token*</code>.
</div>
