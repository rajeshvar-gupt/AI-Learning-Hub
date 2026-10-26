# GEN-001 · Generative model families and objectives

Prerequisites: TR-005. Status: prepared for review.

Outcome: distinguish what each model learns and choose a task-appropriate baseline.

A generative model represents patterns used to produce new samples. An autoregressive language model predicts successive tokens. A VAE combines a latent-variable representation with a reconstruction objective and a distributional regularizer. A GAN trains a generator against a discriminator. A diffusion model learns to reverse a noising process under a specified formulation. These are different training approaches; “generative AI” is not a synonym for one architecture.

Generation quality depends on task, data, objective and evaluation. A plausible output need not be correct. For a course assistant, start with known source passages and explicit unsupported-question behavior before making factual claims about open-ended generation.

The included mock assistant tests plumbing, not learned generation. No GAN/VAE/diffusion training is implemented here. The project's optional Gemini adapter is live-capable code with mocked validation; its real model quality and account access remain untested.

[Questions](../../assignments/GEN-001/questions.md) · [Solutions](../../assignments/GEN-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
