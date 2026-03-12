# Reflection on AI-Assisted Specification Writing

## Introduction
Building CarpoolConnect—an enterprise carpooling platform supporting employee commute logistics and corporate ESG goals—required integrating real-time geo-spatial ride matching, OIDC-compliant authentication, and facility hardware systems. AI-assisted drafting accelerated the specification process but revealed limitations. While AI produced structured documentation quickly, maintaining logical consistency, domain accuracy, and precise technical requirements still required human oversight.

## AI Strengths
AI excelled in early drafting, converting rough ideas into structured outputs such as user stories, API descriptions, and preliminary data models. Outputs often reached 70–80% completeness, reducing the time needed for initial specifications.

The system also demonstrated strong pattern recognition for enterprise architectures. For authentication requirements, AI suggested single sign-on with Okta or Azure AD and outlined user provisioning workflows. It consistently applied structured templates like Role–Goal–Benefit for user stories and produced technical artifacts such as Mermaid.js diagrams.

Strengths were most evident for well-established engineering patterns. Standard REST APIs, authentication workflows, and database schemas were generated clearly and quickly.

**Easier vs Harder Prompt Types**: Output quality directly correlated with prompt structure complexity. **Easier prompts** (broad, pattern-based requests) consistently succeeded. Example: "Draft eight user stories in Role–Goal–Benefit format for a carpooling platform" yielded professional output at ~80% completeness because it leverages well-defined linguistic templates independently. **Harder prompts** (logic-intensive, inter-dependent validation) consistently failed. Example: "Ensure all API endpoint parameters correspond to data model primary keys" produced misaligned results, revealing AI's inability to maintain coherence across sections or "look back" to validate consistency.

## AI Weaknesses
**Real-World Success Example**: When asked to "Design authentication architecture for corporate employee platform," AI independently synthesized SSO integration with Okta and Azure AD, including automatic user provisioning workflows. Success occurred because enterprise SSO is well-established in training data, requiring minimal human guidance.

**Real-World Failure Example**: Requesting "Generate requirements for Sustainability Officers and HR Managers" caused AI to conflate distinct needs. The system merged $CO_2$ aggregate reporting (for ESG compliance—Sustainability Officer need) with employee satisfaction metrics (for HR dashboards) into a single incoherent dashboard. Root cause: AI cannot distinguish semantically different contexts when multiple personas are simultaneously mentioned. Solution: Generate separate specifications per role, then consolidate intentionally.

Terminology inconsistency was frequent: AI labeled the same concept as "Ride," "Trip," or "Booking" across sections—a production catastrophe causing schema misalignment. However, prompt structure influenced output quality significantly. Explicit role identity ("Act as a Senior Systems Architect for enterprise mobility"), environmental context ("closed corporate platform with SSO"), strict negative constraints ("Exclude all consumer social features"), and structural templates ("[Role], [Goal], [Benefit]") all improved consistency measurably. When all four were applied, terminology remained stable; when omitted, AI reverted to generic patterns and pattern bias.

Pattern bias also appeared. Even in closed corporate contexts, AI occasionally suggested consumer-style features like public profiles or social components. Structured prompts reduced filtering needs but did not eliminate them. Vague outputs like "parking optimization" required translation into measurable infrastructure parameters: "QR-based access integration with corporate facility systems" or "within two miles of commute route and ±30-minute window."

Cross-referential validation was unreliable. Tasks like verifying that API parameters matched data models frequently produced inconsistencies. Future improvements could include: maintaining specification registries tracking defined terms and constraints for genuine cross-referential validation; implementing context-aware pattern detection recognizing domain markers ("corporate," "SSO," "ESG") to constrain pattern selection; structuring iterative validation loops as "generate X, then validate against Y" with built-in failure reporting; and generating distinct specification branches per persona with automatic overlap flagging to prevent conflation of separate needs.

## Human Role
Human refinement was essential. Vague AI outputs, such as "find nearby matches," needed translation into precise constraints. Humans grounded abstract features like "parking optimization" in infrastructure, enforced organizational constraints and security standards, and prevented conflation of distinct user needs. For example, generating requirements for Sustainability Officers and HR Managers together produced incoherent outputs; humans resolved this by creating separate persona-specific specifications and consolidating them afterward.

## Lessons Learned
Key lessons include: first, define a glossary to prevent terminology drift. Second, generate requirements per persona independently to avoid conflating distinct needs. Third, decompose complex prompts into smaller, pattern-based tasks for reliability.

Prompt structure profoundly influences AI output quality. Explicit role identity, environmental context, strict negative constraints, and structured templates together reduce pattern bias and maintain consistency. When applied correctly, AI can accelerate drafting and produce high-quality boilerplate content; when omitted, outputs revert to consumer-style assumptions.

Finally, AI is best used as a drafting accelerator, not a final authority. Human expertise remains essential for logical coherence, security compliance, and translating vague business goals into precise technical requirements. Future systems that maintain specification registries, implement context-aware template matching, and generate role-separated outputs with overlap detection could improve reliability. Until then, human oversight of cross-referential logic remains essential.