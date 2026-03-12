# Reflection on AI-Assisted Specification Writing

## Introduction
Building CarpoolConnect—an enterprise carpooling platform designed to support employee commute logistics while advancing corporate ESG sustainability goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. Using AI to assist in writing system specifications accelerated the drafting process but also exposed several limitations. While AI quickly generated structured documentation, maintaining logical consistency, domain accuracy, and precise technical requirements still required significant human oversight.

## AI Strengths
AI was most effective during the early drafting phase of the specification process. It quickly converted rough ideas into structured documentation such as user stories, API endpoint descriptions, and preliminary data models. In many cases, the generated content reached roughly 70–80% completeness, which significantly reduced the time required to produce an initial specification.

The system also demonstrated strong pattern recognition for common enterprise architectures. When describing authentication requirements, for example, the AI independently suggested single sign-on integration with enterprise identity providers such as Okta or Azure AD and outlined user provisioning workflows. It also maintained structured formats like the Role–Goal–Benefit template for user stories and generated technical artifacts such as architecture diagrams using Mermaid.js syntax.

These strengths were most visible when tasks relied on well-established engineering patterns. Standard REST API structures, authentication workflows, and typical database schemas were produced clearly and quickly with minimal prompting. This ability made AI particularly valuable for generating the structural foundation of the specification.

## AI Weaknesses
Several limitations became evident during the process. One recurring issue was terminology inconsistency. The AI sometimes used different labels—such as “Ride,” “Trip,” and “Booking”—for the same concept across different sections. In a real system, this type of drift could lead to mismatched schemas, inconsistent APIs, and confusion during implementation.

Another limitation was pattern bias. Even when the system was clearly defined as a closed corporate platform, the AI occasionally inserted features typical of consumer applications, such as public user profiles or social-style features. These additions conflicted with enterprise security requirements and had to be removed manually.

A more significant weakness appeared when prompts required cross-referencing between sections. When asked to verify that API parameters matched data model fields, the AI often produced inconsistent results. This revealed a limitation in maintaining strict logical alignment across multiple parts of a technical specification.

## Influence of Structure on AI Output
The structure of prompts had a major influence on the quality of AI-generated outputs. Simple, pattern-based prompts consistently produced strong results. For example, asking the AI to generate user stories using a specific template resulted in clear and well-organized outputs.

However, prompts requiring cross-document reasoning or validation were far less reliable. Tasks such as verifying that API parameters matched data model definitions often produced mismatches. The AI performed best when requests were broken into smaller, independent steps rather than requiring complex reasoning across sections of a document.

This experience highlighted the importance of designing prompts with clear structure, constraints, and formatting instructions.

## Human Role
Human refinement was essential in converting AI-generated drafts into reliable specifications. Many AI suggestions were conceptually useful but lacked measurable detail. For instance, vague requirements such as “find nearby matches” needed to be translated into precise constraints like “within two miles of the commute route and within a ±30-minute departure window.”

Humans also grounded abstract features in real infrastructure. Ideas such as “parking optimization” required clarification through specific implementations like QR-based parking access or integration with corporate facility systems.

Most importantly, human review ensured that enterprise security standards and organizational constraints were consistently applied throughout the document.

## Future Improvements
Several improvements could strengthen AI-assisted specification tools. One possibility is the use of terminology registries that track defined system terms and enforce consistent usage across sections. Another improvement would involve stronger context awareness so that domain indicators such as “enterprise” or “corporate environment” guide the AI away from consumer-style features.

AI systems could also benefit from built-in validation mechanisms that compare generated content across sections, helping detect mismatches between APIs, data models, and requirements.

## Lessons Learned
Several key lessons emerged from this process. First, defining a clear glossary before generating content helps prevent terminology drift. Second, generating requirements separately for different user personas reduces the risk of mixing unrelated goals or metrics.

Third, complex prompts requiring validation across multiple sections should be decomposed into smaller tasks. Finally, AI should be treated as a drafting accelerator rather than a final authority. While it can quickly generate structured documentation, human expertise remains essential for logical consistency, security considerations, and ensuring the final specification is coherent and implementable.