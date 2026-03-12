# Reflection on AI-Assisted Specification Writing

## Introduction

Building CarpoolConnect—an enterprise carpooling platform integrating geo-spatial matching, OIDC authentication, and facility hardware—revealed AI's strengths and limitations in specification writing. While AI quickly produced structured documentation, maintaining logical consistency and domain accuracy required human oversight.

## AI Strengths

AI excelled in early drafting, reaching 70–80% completeness on user stories, API descriptions, and data models. It demonstrated strong pattern recognition for enterprise architectures and consistently applied Role–Goal–Benefit templates.

**Easier vs Harder Prompt Types**: Pattern-based prompts succeeded—"Draft eight user stories in Role–Goal–Benefit format" yielded ~80% completion. Logic-intensive prompts failed: "Ensure API parameters match data model keys" produced misaligned results.

## AI Weaknesses and Real-World Examples

### Explicit Success Example
Designing SSO architecture succeeded: the AI synthesized a comprehensive Okta/Azure AD integration with automatic user provisioning and OIDC compliance. Enterprise SSO patterns dominate training data, enabling direct template reuse.

### Explicit Failure Example
Requesting requirements for both Sustainability Officers and HR Managers caused conflation: the AI merged CO₂ aggregate reporting (ESG need) with satisfaction metrics (HR need) into an incoherent dashboard. AI cannot distinguish semantic contexts when multiple personas are mentioned simultaneously.

### Terminology and Bias Issues: How Structure Shapes AI Output

AI labeled identical concepts as "Ride," "Trip," or "Booking" inconsistently. **Systematic testing revealed structure directly controls output consistency**. Four key elements had measurable impact:

**Role Identity** anchored enterprise perspective; **Environmental Context** prevented consumer-app assumptions; **Strict Constraints** blocked pattern bias; **Structural Templates** standardized format. When all four applied, terminology remained stable. When omitted, AI reverted to generic patterns within 2-3 paragraphs. **This demonstrates prompt structure is a control mechanism**, not optional guidance—AI output quality can be engineered through structural constraints.

## Future Improvements for AI Systems

1. **Specification Registries**: Track defined terms, entities, and constraints across documents. Flag "Ride/Trip/Booking" conflation immediately rather than propagating silently.

2. **Context-Aware Pattern Detection**: Recognize domain markers ("corporate," "SSO," "ESG") to constrain patterns beyond consumer defaults. Example: "energy efficiency" triggers HVAC patterns instead of social media features.

3. **Iterative Validation Loops**: Structure validation as "generate X, validate against Y, report failures" with halt conditions. Catch schema misalignment mid-generation rather than after human review.

4. **Persona-Based Generation**: Generate distinct branches per persona with automatic overlap detection. Flag conflicting requirements before consolidation.

## Human Role

Human refinement was essential. Vague outputs needed precise translation. Humans prevented persona conflation by creating separate role-specific specifications and consolidating intentionally.

## Lessons Learned

Define glossaries before generation. Generate requirements per persona independently. Decompose complex prompts into smaller tasks. Prompt structure directly controls output quality—when applied, AI accelerates drafting; when omitted, outputs revert to generic assumptions. AI is best used as a drafting accelerator, not final authority.