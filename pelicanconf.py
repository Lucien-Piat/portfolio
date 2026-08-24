#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic Information
AUTHOR = "Lucien Piat"
SITENAME = "Lucien Piat"
SITESUBTITLE = "Bioinformatics Engineer | Genome assembly & pangenomics"
SITEDESCRIPTION = "Lucien Piat - Bioinformatics Engineer in Zurich, Switzerland, specializing in de novo genome assembly, pangenomics and population genetics."
SITEURL = "https://lucienpiat.fr"

PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"

# Theme
THEME = "themes/portfolio"

# Profile
PROFILE_IMAGE = "images/lucien-piat-bioinformatics-engineer.png"
AUTHOR_EMAIL = "lucienpiat33@gmail.com"
AUTHOR_LOCATION = "Zurich, Switzerland"
FAVICON = "images/favicon.ico"

# Social Links
GITHUB_URL = "https://github.com/Lucien-Piat"
LINKEDIN_URL = "https://www.linkedin.com/in/lucien-piat-47930419b/"
BLUESKY_URL = "https://bsky.app/profile/lpiat.bsky.social"


# About Section
ABOUT_ME = """
I'm a <b>Bioinformatics Engineer</b> currently working at Agroscope (Switzerland) on de novo genome assembly and genetic diversity in grass ecotypes. I recently completed my M.Sc. in Bioinformatics from the University of Rouen, with an 18-month apprenticeship at INRAE.<br><br>

My work centers on <b>pangenomics, genome assembly, and NGS analysis</b>, where I develop computational tools and workflows for large-scale genomic data. These are topics I'm eager to explore further and at greater depth.<br><br>

I also served as House Manager at the Bordeaux National Opera for five years, coordinating reception teams during evening performances, a role that taught me rigor, teamwork, and attention to detail.
"""
# Skills Section
SKILLS = {
    "Bioinformatics": ["Genome Assembly", "Pangenomics ⋆", "NGS", "Workflow Development", "Population Genetics"],
    "Programming": ["Python", "Snakemake", "Bash", "R", "LaTeX"],
    "DevOps & HPC": ["Apptainer", "Cluster Computing", "SLURM, Hetzner", "Git", "CI/CD"],
}

# Projects Section
PROJECTS = [
    {
        "name": "ParaLies",
        "description": "Tool using synonymous divergence (Ks) to detect and remove artefactual duplications caused by failed allelic collapse in heterozygous diploid genome assemblies, while preserving genuine ancient paralogues.",
        "pi": "Dr Anne C. Roulin",
        "tech": ["Python", "Genome Assembly", "DIAMOND", "MCScanX", "Apptainer", "Conda"],
        "github": "https://github.com/Lucien-Piat/ParaLies",
        "images": ["images/paralies-ks-paralogue-detection-genome-assembly.png", "images/paralies-synonymous-divergence-plot.png"],
        "image_alts": [
            "ParaLies Ks-based detection of artefactual duplications from failed allelic collapse in a diploid genome assembly",
            "ParaLies synonymous divergence (Ks) distribution used to remove recent allelic copies while preserving ancient paralogues",
        ],
    },
    {
        "name": "MSpangepop ⋆",
        "description": "Python library for pangenome simulation under coalescent demographic models. Features clean, object-oriented architecture designed for extensibility and ease of use by biologists.",
        "pi": "DSc Ludovic Duvaux",
        "tech": ["Python", "Population Genetics", "Coalescent Theory", "OOP", "MSprime / tskit", "Pangenome Graphs"],
        "github": "https://github.com/inrae/MSpangepop",
        "gitlab": "https://forge.inrae.fr/pangepop/MSpangepop/",
        "extra": ("Poster", "pdfs/02_Piat_et_al_Jul_2025.pdf"),
        "images": ["images/mspangepop-pangenome-simulation-coalescent.svg"],
        "image_alts": [
            "MSpangepop workflow for simulating population pangenomes under coalescent demographic models",
        ],
    },
    {
        "name": "Asm4gp ⋆",
        "description": "Comprehensive long-read assembly and QC pipeline supporting PacBio, ONT, TRIO, Hi-C, and HiFi data. Developed using Snakemake to automate haplotype-resolved genome assembly inputs for pangenome construction.",
        "pi": "DSc Ludovic Duvaux",
        "tech": ["Snakemake", "Python", "SLURM", "Apptainer", "Conda", "Bash"],
        "github": "https://github.com/inrae/GenomAsm4pg",
        "gitlab": "https://forge.inrae.fr/asm4pg/GenomAsm4pg/",
        "extra": ("Annimated flowchart", "https://asm4pg-animated-7dc863.pages-forge.inrae.fr/asm4pg_animated.html"),
        "images": ["images/asm4pg-long-read-genome-assembly-pipeline.png", "images/asm4pg-snakemake-haplotype-assembly.png"],
        "image_alts": [
            "Asm4pg long-read genome assembly and QC pipeline supporting PacBio, ONT, Hi-C and HiFi data",
            "Asm4pg Snakemake workflow producing haplotype-resolved genome assemblies for pangenome construction",
        ],
    },
]

# Smaller projects, rendered as compact half-width cards with a single image
SMALL_PROJECTS = [
    {
        "name": "MycoLasso",
        "description": "MycoLasso is a Shiny GUI app to load, visualize, and interactively explore geospatial data points.",
        "tech": ["R", "Shiny", "Leaflet"],
        "github": "https://github.com/Lucien-Piat/MycoLasso",
        "extra": ("Website", "https://lucien-piat.shinyapps.io/mycolasso/"),
        "images": ["images/mycolasso-shiny-geospatial-visualization.png", "images/mycolasso-interactive-leaflet-map.png"],
        "image_alts": [
            "MycoLasso R Shiny app visualizing geospatial data points",
            "MycoLasso interactive Leaflet map for exploring geospatial data",
        ],
    },
    {
        "name": "Urban Tree Detection",
        "description": " U-Net Deep learning pipeline for tree detection and counting from satellite imagery.",
        "pi": "Pr Jean-Christophe Taveau",
        "tech": ["Computer Vision", "Python", "Deep Learning"],
        "extra": ("Report", "pdfs/DLF_report.pdf"),
        "images": ["images/urban-tree-detection-unet-satellite-imagery.png", "images/urban-tree-detection-deep-learning-segmentation.png"],
        "image_alts": [
            "Urban tree detection from satellite imagery using a U-Net deep learning architecture",
            "Deep learning segmentation results for automated urban tree detection and counting",
        ],
    },
    {
        "name": "FEAther",
        "description": "Shiny GUI for functional enrichment analysis of biological data.",
        "pi": "Asst. Prof Hélène Dauchel",
        "tech": ["R", "Shiny", "Functional Enrichment Analysis"],
        "github": "https://github.com/Lucien-Piat/FEAther",
        "extra": ("Website", "https://lucien-piat.shinyapps.io/feather/"),
        "images": ["images/feather-functional-enrichment-analysis-shiny.png", "images/feather-enrichment-visualization-plots.png"],
        "image_alts": [
            "FEAther R Shiny app for functional enrichment analysis of biological data",
            "FEAther interactive plots and tables visualizing functional enrichment results",
        ],
    },
    {
        "name": "Fruit Proteomics Analysis",
        "pi": "Dr Sophie Colombié",
        "description": "Statistical analysis of proteomic data across five fruit species.",
        "tech": ["R", "Functional Enrichment Analysis", "Proteomics"],
        "images": ["images/fruit-proteomics-differential-expression-analysis.png", "images/fruit-proteomics-r-statistical-analysis.png"],
        "image_alts": [
            "Fruit proteomics differential protein expression analysis across five species",
            "Statistical analysis in R of the fruit proteome across developmental stages",
        ],
    },
]

WORK_EXPERIENCE = [
    {
        "title": "Bioinformatics Engineer Intern",
        "company": "Agroscope - Wädenswil, Switzerland",
        "period": "Apr 2026 - <i>Now ⭐</i>",
        "description": "De novo genome assembly and genetic diversity analyses in Swiss ecotypes of <i>Lolium multiflorum</i>.",
    },
    {
        "title": "Bioinformatics M.Sc. Engineer Apprentice",
        "company": "INRAE BIOGECO - Cestas, France",
        "period": "2024 - 2026",
        "description": "Developing pangenomics tools and workflows to help identify structural variants in <i>Quercus spp.</i>.",
    },
    {
        "title": "Proteomics B.Sc. Research Intern",
        "company": "INRAE BFP - Villenave-d'Ornon, France",
        "period": "May - June 2023",
        "description": "Statistical analysis of fruit proteome across 5 species, identifying differential expression patterns across developmental stages.",
    },
]

EDUCATION = [
    {"degree": "M.Sc. Bioinformatics, Modeling and Statistics", "institution": "University of Rouen Normandy", "period": "2024 - 2026", "note": "2nd year of M.Sc. 18-month apprenticeship program"},
    {
        "degree": "Deep Learning Research Exchange",
        "institution": "University of Groningen - Netherlands",
        "period": "Jan - May 2024",
        "note": "Deep learning of satellite imagery applied to urban forestry",
    },
    {"degree": "M.Sc. Bioinformatics", "institution": "University of Bordeaux", "period": "2023 - 2024", "note": "1st year of M.Sc."},
    {"degree": "B.Sc. Life Sciences", "institution": "University of Bordeaux", "period": "2021 - 2023", "note": None},
]

PUBLICATIONS = [
    {
        "title": "(preprint) A chromosome-scale genome assembly of the Swiss Lolium multiflorum ecotype Tremona reveals a scalable method to purge spurious duplications",
        "authors": "<b>L. Piat</b>, G. Herren, C. Grieder, A.C. Roulin",
        "venue": "bioRxiv, 2026",
        "link": "https://www.biorxiv.org/content/10.64898/2026.08.18.745395v1",
        "link_label": "bioRxiv",
    },
    {
        "title": "(preprint) Simulating population pangenomes under coalescent demographic models with MSpangenome",
        "authors": "<b>L. Piat</b>, S. Denni, S. Dubois, B. Linard, L. Duvaux",
        "venue": "bioRxiv, 2026",
        "link": "https://www.biorxiv.org/content/10.64898/2026.06.29.735168v1",
        "link_label": "bioRxiv",
    },
    {
        "title": "(preprint) A reference genome assembly for Quercus canariensis Willd",
        "authors": "F. Couturier, C. Cravero, I. Lesur, J. Confais, E. Belmonte, <b>L. Piat</b>, W. Marande, C. Rellstab, M. Valbuena, E. Saez-Laguna, L. Duvaux",
        "venue": "bioRxiv, 2026",
        "link": "https://www.biorxiv.org/content/10.64898/2026.03.31.714748v2",
        "link_label": "bioRxiv",
    },
]

POSTERS = [
    {
        "title": "MSpangepop: Simulating complex structural variants under advanced demographic scenarios using the coalescent",
        "authors": "<b>L. Piat</b>, S. Denni, S. Dubois, F. Couturier, N. Lapalu, B. Linard, C. Lemaitre, L. Duvaux",
        "venue": "JOBIM 2025, Bordeaux, France",
        "link": "https://hal.science/hal-05219528",
        "link_label": "HAL",
    }
]

REPORTS = [
    {
        "title": "De la construction a la simulation des pangenomes : une approche bioinformatique integree via Asm4pg et MSpangepop",
        "context": "M.Sc. apprenticeship report, INRAE BIOGECO / Univ. Rouen, 2024-2026",
        "supervisor": "Dr. Ludovic Duvaux",
        "link": "pdfs/rapport_alternance_M2_2_bims.pdf",
    },
    {
        "title": "Single Tree Detection: The Jurassic Bark",
        "context": "Erasmus+ research project, University of Groningen, March 2024",
        "authors": "M. Nurmukhambetov, C. Salzmann, K. Verhaeghe, L. Piat",
        "link": "pdfs/DLF_report.pdf",
    },
]

# Static files
STATIC_PATHS = [
    "images",
    "extras",
    "extras/CNAME",
    "extras/sitemap.xml",
    "extras/robots.txt",
    "pdfs",
]

EXTRA_PATH_METADATA = {"extras/CNAME": {"path": "CNAME"}, "extras/sitemap.xml": {"path": "sitemap.xml"}, "extras/robots.txt": {"path": "robots.txt"}}

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
READERS = {"html": None}
# Disable unnecessary page generation
DIRECT_TEMPLATES = ["index"]
PAGINATED_TEMPLATES = {}

RELATIVE_URLS = True
