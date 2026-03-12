# Reflection on AI-Assisted Specification Writing

## Introduction

Building CarpoolConnect—an enterprise carpooling platform supporting employee commute logistics while advancing corporate ESG sustainability goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. Using AI to assist with writing system specifications accelerated the drafting process but also revealed limitations. While AI quickly generated structured documentation, maintaining logical consistency, domain accuracy, and precise technical requirements still required human oversight.

## AI Strengths

AI was most effective during the early drafting phase of the specification process. It rapidly converted rough ideas into structured documentation such as user stories, API endpoint descriptions, and preliminary data models. In many cases, outputs reached roughly 70–80% completeness, significantly reducing the time needed to produce an initial specification.

The system also demonstrated strong pattern recognition for common enterprise architectures. When describing authentication requirements, for example, the AI independently suggested single sign-on integration with enterprise identity providers such as Okta or Azure AD and outlined user provisioning workflows. It consistently generated structured formats like the Role–Goal–Benefit template for user stories and produced technical artifacts such as architecture diagrams using Mermaid.js syntax.

These strengths were most evident when tasks relied on established engineering patterns. Standard REST API structures, authentication workflows, and typical database schemas were generated clearly with minimal prompting. This capability made AI particularly useful for building the structural foundation of the specification.

## AI Weaknesses

Several limitations became evident during the process. One recurring issue was terminology inconsistency. The AI sometimes used different labels—such as “Ride,” “Trip,” and “Booking”—for the same concept across sections. In a real system, this drift could cause mismatched schemas, inconsistent APIs, and implementation confusion.

Another limitation was pattern bias. Even when the system was clearly defined as a closed corporate platform, the AI occasionally inserted consumer-style features such as public user profiles or social components. These conflicted with enterprise security requirements and required manual removal.

A more significant weakness appeared when prompts required cross-referencing between sections. When asked to verify that API parameters matched data model fields, the AI frequently produced inconsistent results. This highlighted a limitation in maintaining strict logical alignment across multiple parts of a technical specification.

## Human Role

Human refinement was essential in converting AI-generated drafts into reliable specifications. Many AI suggestions were conceptually useful but lacked measurable detail. For example, vague requirements like “find nearby matches” needed translation into precise constraints such as “within two miles of the commute route and within a ±30-minute departure window.”

Humans also grounded abstract features in real infrastructure. Concepts like “parking optimization” required clarification through specific implementations such as QR-based parking access or integration with corporate facility systems.

Most importantly, human review ensured enterprise security standards and organizational constraints were applied consistently throughout the document.

## Lessons Learned

Several key lessons emerged from this process. First, defining a clear glossary before generation helps prevent terminology drift. Second, generating requirements separately for different user personas reduces the risk of mixing unrelated goals or metrics.

Third, complex prompts requiring cross-section validation should be decomposed into smaller tasks. Finally, AI should be treated as a drafting accelerator rather than a final authority. While it can quickly generate structured documentation, human expertise remains essential for logical consistency, security considerations, and ensuring the final specification is coherent and implementable.