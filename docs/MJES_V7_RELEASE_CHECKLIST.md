# Pre-release checks for MJES v7 supporting materials

- [x] Confirm review procedure with authors: Zaher Fadhil Raham and Sura Salah selected and assessed studies by joint agreement, **without independent screening** (confirmed 11 November 2026). No inter-rater statistic is claimed.
- [ ] Verify the 207 imported / 26 duplicate / 181 unique counts against frozen original exports, distinguishing imported origins from deduplicated origins.
- [ ] Validate bibliography provenance, DOIs, titles and source URLs; do not claim 181 included studies.
- [ ] Check whether Scopus, IEEE Xplore and ScienceDirect metadata export terms permit public redistribution of each proposed column.
- [ ] Avoid depositing copyrighted article PDFs, original abstracts or other restricted content.
- [ ] Confirm E1–E4 evidence classifications against the manual appraisal source. The category codebook alone is not classified study data.
- [ ] Include provenance of each released table, license scope, original metadata acquisition information and SHA-256 manifest.
- [ ] Confirm authorship, affiliations, corresponding author and funding/declarations in the submitted manuscript.
- [ ] Correct or regenerate `metadata/release_manifest.json` for the *actual* release commit. The existing manifest declares v0.1.0 and contains hashes/byte sizes inconsistent with present files; do not treat it as a verified v0.2.0 inventory.
- [ ] Review `data/scopus_abstract_provenance_93.csv` and `data/source_linked_scopus_76.csv` for third-party abstract provenance and permitted reuse before archiving. Some entries refer to full abstracts in licensed exports.
- [ ] Ensure `docs/REPORTING_SCOPE.md` uses the confirmed two-researcher consensus procedure (updated on the review branch).
- [ ] Confirm the basic CSV integrity script passes. Do not call it empirical validation of the framework.
- [ ] Complete GitHub release and connect Zenodo; record the exact DOI and immutable version URL only once issued.
- [ ] Replace [repository URL] in Section “Data and Materials Availability” using the actual public release link.
- [ ] Avoid describing repository existence as journal acceptance or publication.

No GitHub release or Zenodo DOI is asserted by this checklist.
