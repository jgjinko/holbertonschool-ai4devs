# Reflection on AI-Assisted Specification Writing

## Introduction

The development of the CarpoolConnect specification served as a rigorous case study in human-AI collaboration. CarpoolConnect is not merely a ride-sharing app; it is a complex enterprise ecosystem designed to bridge the gap between employee logistics and corporate ESG (Environmental, Social, and Governance) targets. In the corporate landscape of 2026, mapping out a platform that integrates real-time geo-spatial matching with corporate SSO and physical facility hardware requires a level of precision that tests the boundaries of generative AI. This reflection analyzes the journey of transforming a high-level concept into a structured technical blueprint, evaluating how prompt structures and human intervention influenced the final output.

## AI Strengths: The Accelerant of Structure

The most immediate benefit of utilizing AI in this process was its capacity for rapid structural scaffolding. AI effectively neutralized the "blank page" problem by instantly synthesizing raw ideas into standardized industry formats like "User Stories" and "API Specifications." It functioned as a high-speed drafting engine, providing a foundation that was roughly 75% complete in a matter of seconds.

Specifically, the AI excelled at architectural intuition. Without being explicitly prompted, it recognized that an enterprise carpooling app would require an OIDC-compliant Authentication Service and a geo-spatial Matching Engine. Its ability to maintain syntactic consistency—such as the "Role-Goal-Benefit" format for user stories—ensured that the documentation remained professional and readable. Furthermore, the integration of LaTeX for technical variables like $CO_2$ and mathematical range constraints (e.g., ± 30 minutes) added a level of scientific precision that is often overlooked in manual drafting. The generation of Mermaid.js code for system diagrams was another standout success, allowing for a visual representation of the data flow that would traditionally require specialized design software.

## AI Weaknesses: Terminological Drift and Pattern Bias

Despite its speed, the AI displayed significant terminological drift and pattern-matching bias. A recurring issue was the lack of "internal consistency" across different sections of the document. Because the AI processes text as a series of independent statistical probabilities rather than a unified logical model, it often failed to maintain "Domain Isolation." For instance, it would define a primary data entity as a "Ride" in the user stories but refer to it as a "Trip" or "Booking" within the API endpoints. In a production environment, this inconsistency is a critical failure; if a database schema uses one term while the frontend uses another, the integration process becomes a debugging nightmare.

The AI also suffered from "feature bloat" or "hallucinated social patterns." It frequently attempted to insert generic social media features—such as "public profiles" or "friend requests"—which contradicted the "walled-garden" corporate security context defined in the brief. This suggests that the AI often defaults to the most common patterns in its training data (consumer-facing apps) rather than adhering strictly to the specific logical constraints of the project (enterprise software).

## The Influence of Prompt Structure

The quality of the AI's output was directly proportional to the granularity and hierarchy of the prompt structure. We observed a clear divide between prompt types based on how much inter-dependency was required.

### Easier vs. Harder Prompts

**Easier Prompts (High Success)**: Broad structural requests following known patterns yielded excellent results. For example, asking the AI to "Draft 8 user stories in Role-Goal-Benefit format" produced a consistent, professional list because the AI was following a well-defined linguistic template.

**Harder Prompts (Low Success)**: Logic-intensive, inter-dependent requests often failed. When I prompted the AI to "Ensure API parameters in section 4 match primary keys in the Data Model in section 3," the results were inconsistent. The AI struggles to "look back" at previous definitions to ensure functional alignment across different technical domains.

### Key Prompt Elements

To achieve high-fidelity specifications, a prompt must contain four pillars:

- **Role Identity**: Explicitly telling the AI to "Act as a Senior Systems Architect" or "Sustainability Consultant."
- **Environmental Context**: Providing specific boundaries like "This is a closed-loop corporate environment using SSO."
- **Strict Constraints**: Using negative constraints such as "Provide exactly 3 unique features; exclude generic social media functions."
- **Structural Templates**: Giving the AI the exact format to follow, such as "Format user stories as [Role], [Goal], [Benefit]."

## Real-World Success and Failure Examples

**Success Case**: The AI perfectly mapped the relationship between the Auth Service and corporate Identity Providers like Okta and Azure AD. It recognized the enterprise requirement for Single Sign-On (SSO) and automatic user provisioning without needing a detailed explanation of enterprise security logic.

**Failure Case**: The AI initially failed to differentiate between the data needs of a Sustainability Officer (who requires aggregate, verifiable $CO_2$ data for ESG reporting) and an HR Manager (who requires individual employee satisfaction and retention metrics). It attempted to blend these into a single, confusing dashboard, requiring significant human intervention to separate the two distinct business objectives.

## The Human Role: Logical Gatekeeper

Manual refinement was not just helpful; it was the "Logical Gatekeeper" of the entire process. While the AI generated the text, the human provided the precision. My primary role was to strip away the AI's polite filler and replace it with testable, hard requirements.

For example, when the AI suggested users find "nearby" matches, I refined this into a specific technical constraint: "within a 2-mile radius of the commute path." This transition from a qualitative goal to a quantitative requirement is where human judgment is indispensable. I also had to enforce security boundaries, ensuring that the "Parking Optimization" feature was explicitly linked to physical facility hardware via QR codes, rather than being left as a vague software concept. The human role has shifted from writing the document to editing for intent.

## Recommendations and Conclusion

For future work, I recommend a "Glossary-First" approach: define immutable terms (e.g., "User," "Trip," "Organization") at the session start to force terminological consistency. Additionally, employing Chain-of-Thought prompting—asking the AI to outline the mathematical logic of a feature before writing the user stories—leads to far more cohesive acceptance criteria.

In conclusion, AI is a powerful accelerant for specification writing, but the human remains the architect. The most effective path forward leverages AI's speed for boilerplate documentation while reserving human cognitive energy for the complex logic, security constraints, and the judgment that defines successful enterprise products.