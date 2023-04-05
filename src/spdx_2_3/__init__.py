# generated by datamodel-codegen:
#   filename:  spdx-schema.json
#   timestamp: 2023-04-05T08:38:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field


class AnnotationType(str, Enum):
    other = "OTHER"
    review = "REVIEW"


class Annotation(BaseModel):
    class Config:
        extra = Extra.forbid

    annotation_date: str = Field(
        ...,
        alias="annotationDate",
        description=(
            "Identify when the comment was made. This is to be specified according to"
            " the combined date and time in the UTC format, as specified in the ISO"
            " 8601 standard."
        ),
    )
    annotation_type: AnnotationType = Field(
        ..., alias="annotationType", description="Type of the annotation."
    )
    annotator: str = Field(
        ...,
        description=(
            "This field identifies the person, organization, or tool that has commented"
            " on a file, package, snippet, or the entire document."
        ),
    )
    comment: str


class CreationInfo(BaseModel):
    class Config:
        extra = Extra.forbid

    comment: Optional[str]
    created: str = Field(
        ...,
        description=(
            "Identify when the SPDX document was originally created. The date is to be"
            " specified according to combined date and time in UTC format as specified"
            " in ISO 8601 standard."
        ),
    )
    creators: list[str] = Field(
        ...,
        description=(
            "Identify who (or what, in the case of a tool) created the SPDX document."
            " If the SPDX document was created by an individual, indicate the person's"
            " name. If the SPDX document was created on behalf of a company or"
            " organization, indicate the entity name. If the SPDX document was created"
            " using a software tool, indicate the name and version for that tool. If"
            " multiple participants or tools were involved, use multiple instances of"
            " this field. Person name or organization name may be designated as"
            " “anonymous” if appropriate."
        ),
        min_items=1,
    )
    license_list_version: Optional[str] = Field(
        default=None,
        alias="licenseListVersion",
        description=(
            "An optional field for creators of the SPDX file to provide the version of"
            " the SPDX License List used when the SPDX file was created."
        ),
    )


class Algorithm(str, Enum):
    sha1 = "SHA1"
    blake3 = "BLAKE3"
    sha3_384 = "SHA3-384"
    sha256 = "SHA256"
    sha384 = "SHA384"
    blake2b_512 = "BLAKE2b-512"
    blake2b_256 = "BLAKE2b-256"
    sha3_512 = "SHA3-512"
    md2 = "MD2"
    adler32 = "ADLER32"
    md4 = "MD4"
    sha3_256 = "SHA3-256"
    blake2b_384 = "BLAKE2b-384"
    sha512 = "SHA512"
    md6 = "MD6"
    md5 = "MD5"
    sha224 = "SHA224"


class Checksum(BaseModel):
    class Config:
        extra = Extra.forbid

    algorithm: Algorithm = Field(
        ...,
        description=(
            "Identifies the algorithm used to produce the subject Checksum. Currently,"
            " SHA-1 is the only supported algorithm. It is anticipated that other"
            " algorithms will be supported at a later time."
        ),
    )
    checksum_value: str = Field(
        ...,
        alias="checksumValue",
        description=(
            "The checksumValue property provides a lower case hexidecimal encoded"
            " digest value produced using a specific algorithm."
        ),
    )


class ExternalDocumentRef(BaseModel):
    class Config:
        extra = Extra.forbid

    checksum: Checksum = Field(
        ...,
        description=(
            "A Checksum is value that allows the contents of a file to be"
            " authenticated. Even small changes to the content of the file will change"
            " its checksum. This class allows the results of a variety of checksum and"
            " cryptographic message digest algorithms to be represented."
        ),
    )
    external_document_id: str = Field(
        ...,
        alias="externalDocumentId",
        description=(
            "externalDocumentId is a string containing letters, numbers, ., - and/or +"
            " which uniquely identifies an external document within this document."
        ),
    )
    spdx_document: str = Field(
        ...,
        alias="spdxDocument",
        description=("SPDX ID for SpdxDocument.  A property containing an SPDX document."),
    )


class CrossRef(BaseModel):
    class Config:
        extra = Extra.forbid

    is_live: Optional[bool] = Field(
        default=None,
        alias="isLive",
        description=("Indicate a URL is still a live accessible location on the public internet"),
    )
    is_valid: Optional[bool] = Field(
        default=None,
        alias="isValid",
        description="True if the URL is a valid well formed URL",
    )
    is_way_back_link: Optional[bool] = Field(
        default=None,
        alias="isWayBackLink",
        description="True if the License SeeAlso URL points to a Wayback archive",
    )
    match: Optional[str] = Field(
        default=None,
        description=(
            "Status of a License List SeeAlso URL reference if it refers to a website"
            " that matches the license text."
        ),
    )
    order: Optional[int] = Field(
        default=None, description="The ordinal order of this element within a list"
    )
    timestamp: Optional[str] = Field(default=None, description="Timestamp")
    url: str = Field(..., description="URL Reference")


class HasExtractedLicensingInfo(BaseModel):
    class Config:
        extra = Extra.forbid

    comment: Optional[str]
    cross_refs: Optional[list[CrossRef]] = Field(
        default=None,
        alias="crossRefs",
        description="Cross Reference Detail for a license SeeAlso URL",
    )
    extracted_text: str = Field(
        ...,
        alias="extractedText",
        description=(
            "Provide a copy of the actual text of the license reference extracted from"
            " the package, file or snippet that is associated with the License"
            " Identifier to aid in future analysis."
        ),
    )
    license_id: str = Field(
        ...,
        alias="licenseId",
        description=(
            "A human readable short form license identifier for a license. The license"
            " ID is either on the standard license list or the form"
            ' "LicenseRef-[idString]" where [idString] is a unique string containing'
            ' letters, numbers, "." or "-".  When used within a license expression, the'
            " license ID can optionally include a reference to an external document in"
            ' the form "DocumentRef-[docrefIdString]:LicenseRef-[idString]" where'
            " docRefIdString is an ID for an external document reference."
        ),
    )
    name: Optional[str] = Field(default=None, description="Identify name of this SpdxElement.")
    see_alsos: Optional[list[str]] = Field(default=None, alias="seeAlsos")


class Reviewed(BaseModel):
    class Config:
        extra = Extra.forbid

    comment: Optional[str]
    review_date: str = Field(
        ...,
        alias="reviewDate",
        description=(
            "The date and time at which the SpdxDocument was reviewed. This value must"
            " be in UTC and have 'Z' as its timezone indicator."
        ),
    )
    reviewer: Optional[str] = Field(
        default=None,
        description=(
            "The name and, optionally, contact information of the person who performed"
            " the review. Values of this property must conform to the agent and tool"
            " syntax.  The reviewer property is deprecated in favor of Annotation with"
            " an annotationType review."
        ),
    )


class Annotation1(Annotation):
    pass


class Checksum1(Checksum):
    pass


class ReferenceCategory(str, Enum):
    other = "OTHER"
    persistent_id = "PERSISTENT-ID"
    security = "SECURITY"
    package_manager = "PACKAGE-MANAGER"


class ExternalRef(BaseModel):
    class Config:
        extra = Extra.forbid

    comment: Optional[str]
    reference_category: ReferenceCategory = Field(
        ...,
        alias="referenceCategory",
        description="Category for the external reference",
    )
    reference_locator: str = Field(
        ...,
        alias="referenceLocator",
        description=(
            "The unique string with no spaces necessary to access the package-specific"
            " information, metadata, or content within the target location. The format"
            " of the locator is subject to constraints defined by the <type>."
        ),
    )
    reference_type: str = Field(
        ...,
        alias="referenceType",
        description=(
            "Type of the external reference. These are definined in an appendix in the"
            " SPDX specification."
        ),
    )


class PackageVerificationCode(BaseModel):
    class Config:
        extra = Extra.forbid

    package_verification_code_excluded_files: Optional[list[str]] = Field(
        default=None,
        alias="packageVerificationCodeExcludedFiles",
        description=(
            "A file that was excluded when calculating the package verification code."
            " This is usually a file containing SPDX data regarding the package. If a"
            " package contains more than one SPDX file all SPDX files must be excluded"
            " from the package verification code. If this is not done it would be"
            " impossible to correctly calculate the verification codes in both files."
        ),
    )
    package_verification_code_value: str = Field(
        ...,
        alias="packageVerificationCodeValue",
        description="The actual package verification code as a hex encoded value.",
    )


class PrimaryPackagePurpose(str, Enum):
    other = "OTHER"
    install = "INSTALL"
    archive = "ARCHIVE"
    firmware = "FIRMWARE"
    application = "APPLICATION"
    framework = "FRAMEWORK"
    library = "LIBRARY"
    container = "CONTAINER"
    source = "SOURCE"
    device = "DEVICE"
    operating_system = "OPERATING_SYSTEM"
    file = "FILE"


class Package(BaseModel):
    class Config:
        extra = Extra.forbid

    spdxid: str = Field(
        ...,
        alias="SPDXID",
        description=(
            "Uniquely identify any element in an SPDX document which may be referenced"
            " by other elements."
        ),
    )
    annotations: Optional[list[Annotation1]] = Field(
        default=None, description="Provide additional information about an SpdxElement."
    )
    attribution_texts: Optional[list[str]] = Field(
        default=None,
        alias="attributionTexts",
        description=(
            "This field provides a place for the SPDX data creator to record"
            " acknowledgements that may be required to be communicated in some"
            " contexts. This is not meant to include the actual complete license text"
            " (see licenseConculded and licenseDeclared), and may or may not include"
            " copyright notices (see also copyrightText). The SPDX data creator may use"
            " this field to record other acknowledgements, such as particular clauses"
            " from license texts, which may be necessary or desirable to reproduce."
        ),
    )
    built_date: Optional[str] = Field(
        default=None,
        alias="builtDate",
        description=(
            "This field provides a place for recording the actual date the package was" " built."
        ),
    )
    checksums: Optional[list[Checksum1]] = Field(
        default=None,
        description=(
            "The checksum property provides a mechanism that can be used to verify that"
            " the contents of a File or Package have not changed."
        ),
    )
    comment: Optional[str]
    copyright_text: Optional[str] = Field(
        default=None,
        alias="copyrightText",
        description=(
            "The text of copyright declarations recited in the package, file or"
            " snippet.\n\nIf the copyrightText field is not present, it implies an"
            " equivalent meaning to NOASSERTION."
        ),
    )
    description: Optional[str] = Field(
        default=None, description="Provides a detailed description of the package."
    )
    download_location: str = Field(
        ...,
        alias="downloadLocation",
        description=(
            "The URI at which this package is available for download. Private (i.e.,"
            " not publicly reachable) URIs are acceptable as values of this property."
            " The values http://spdx.org/rdf/terms#none and"
            " http://spdx.org/rdf/terms#noassertion may be used to specify that the"
            " package is not downloadable or that no attempt was made to determine its"
            " download location, respectively."
        ),
    )
    external_refs: Optional[list[ExternalRef]] = Field(
        default=None,
        alias="externalRefs",
        description=(
            "An External Reference allows a Package to reference an external source of"
            " additional information, metadata, enumerations, asset identifiers, or"
            " downloadable content believed to be relevant to the Package."
        ),
    )
    files_analyzed: Optional[bool] = Field(
        default=None,
        alias="filesAnalyzed",
        description=(
            "Indicates whether the file content of this package has been available for"
            " or subjected to analysis when creating the SPDX document. If false"
            " indicates packages that represent metadata or URI references to a"
            " project, product, artifact, distribution or a component. If set to false,"
            " the package must not contain any files."
        ),
    )
    has_files: Optional[list[str]] = Field(
        default=None,
        alias="hasFiles",
        description="Indicates that a particular file belongs to a package.",
    )
    homepage: Optional[str]
    license_comments: Optional[str] = Field(
        default=None,
        alias="licenseComments",
        description=(
            "The licenseComments property allows the preparer of the SPDX document to"
            " describe why the licensing in spdx:licenseConcluded was chosen."
        ),
    )
    license_concluded: Optional[str] = Field(
        default=None,
        alias="licenseConcluded",
        description=(
            "License expression for licenseConcluded. See SPDX Annex D for the license"
            " expression syntax.  The licensing that the preparer of this SPDX document"
            " has concluded, based on the evidence, actually applies to the SPDX"
            " Item.\n\nIf the licenseConcluded field is not present for an SPDX Item,"
            " it implies an equivalent meaning to NOASSERTION."
        ),
    )
    license_declared: Optional[str] = Field(
        default=None,
        alias="licenseDeclared",
        description=(
            "License expression for licenseDeclared. See SPDX Annex D for the license"
            " expression syntax.  The licensing that the creators of the software in"
            " the package, or the packager, have declared. Declarations by the original"
            " software creator should be preferred, if they exist."
        ),
    )
    license_info_from_files: Optional[list[str]] = Field(
        default=None,
        alias="licenseInfoFromFiles",
        description=(
            "The licensing information that was discovered directly within the package."
            " There will be an instance of this property for each distinct value of"
            " alllicenseInfoInFile properties of all files contained in the"
            " package.\n\nIf the licenseInfoFromFiles field is not present for a"
            " package and filesAnalyzed property for that same pacakge is true or"
            " omitted, it implies an equivalent meaning to NOASSERTION."
        ),
    )
    name: str = Field(..., description="Identify name of this SpdxElement.")
    originator: Optional[str] = Field(
        default=None,
        description=(
            "The name and, optionally, contact information of the person or"
            " organization that originally created the package. Values of this property"
            " must conform to the agent and tool syntax."
        ),
    )
    package_file_name: Optional[str] = Field(
        default=None,
        alias="packageFileName",
        description=("The base name of the package file name. For example, zlib-1.2.5.tar.gz."),
    )
    package_verification_code: Optional[PackageVerificationCode] = Field(
        default=None,
        alias="packageVerificationCode",
        description=(
            "A manifest based verification code (the algorithm is defined in section"
            " 4.7 of the full specification) of the SPDX Item. This allows consumers of"
            " this data and/or database to determine if an SPDX item they have in hand"
            " is identical to the SPDX item from which the data was produced. This"
            " algorithm works even if the SPDX document is included in the SPDX item."
        ),
    )
    primary_package_purpose: Optional[PrimaryPackagePurpose] = Field(
        default=None,
        alias="primaryPackagePurpose",
        description=(
            "This field provides information about the primary purpose of the"
            " identified package. Package Purpose is intrinsic to how the package is"
            " being used rather than the content of the package."
        ),
    )
    release_date: Optional[str] = Field(
        default=None,
        alias="releaseDate",
        description=(
            "This field provides a place for recording the date the package was" " released."
        ),
    )
    source_info: Optional[str] = Field(
        default=None,
        alias="sourceInfo",
        description=(
            "Allows the producer(s) of the SPDX document to describe how the package"
            " was acquired and/or changed from the original source."
        ),
    )
    summary: Optional[str] = Field(
        default=None, description="Provides a short description of the package."
    )
    supplier: Optional[str] = Field(
        default=None,
        description=(
            "The name and, optionally, contact information of the person or"
            " organization who was the immediate supplier of this package to the"
            " recipient. The supplier may be different than originator when the"
            " software has been repackaged. Values of this property must conform to the"
            " agent and tool syntax."
        ),
    )
    valid_until_date: Optional[str] = Field(
        default=None,
        alias="validUntilDate",
        description=(
            "This field provides a place for recording the end of the support period"
            " for a package from the supplier."
        ),
    )
    version_info: Optional[str] = Field(
        default=None,
        alias="versionInfo",
        description=(
            "Provides an indication of the version of the package that is described by"
            " this SpdxDocument."
        ),
    )


class Annotation2(Annotation):
    pass


class Checksum2(Checksum):
    pass


class FileType(str, Enum):
    other = "OTHER"
    documentation = "DOCUMENTATION"
    image = "IMAGE"
    video = "VIDEO"
    archive = "ARCHIVE"
    spdx = "SPDX"
    application = "APPLICATION"
    source = "SOURCE"
    binary = "BINARY"
    text = "TEXT"
    audio = "AUDIO"


class File(BaseModel):
    class Config:
        extra = Extra.forbid

    spdxid: str = Field(
        ...,
        alias="SPDXID",
        description=(
            "Uniquely identify any element in an SPDX document which may be referenced"
            " by other elements."
        ),
    )
    annotations: Optional[list[Annotation2]] = Field(
        default=None, description="Provide additional information about an SpdxElement."
    )
    artifact_ofs: Optional[list[dict[str, Any]]] = Field(
        default=None,
        alias="artifactOfs",
        description=(
            "Indicates the project in which the SpdxElement originated. Tools must"
            " preserve doap:homepage and doap:name properties and the URI (if one is"
            " known) of doap:Project resources that are values of this property. All"
            " other properties of doap:Projects are not directly supported by SPDX and"
            " may be dropped when translating to or from some SPDX formats."
        ),
    )
    attribution_texts: Optional[list[str]] = Field(
        default=None,
        alias="attributionTexts",
        description=(
            "This field provides a place for the SPDX data creator to record"
            " acknowledgements that may be required to be communicated in some"
            " contexts. This is not meant to include the actual complete license text"
            " (see licenseConculded and licenseDeclared), and may or may not include"
            " copyright notices (see also copyrightText). The SPDX data creator may use"
            " this field to record other acknowledgements, such as particular clauses"
            " from license texts, which may be necessary or desirable to reproduce."
        ),
    )
    checksums: list[Checksum2] = Field(
        ...,
        description=(
            "The checksum property provides a mechanism that can be used to verify that"
            " the contents of a File or Package have not changed."
        ),
        min_items=1,
    )
    comment: Optional[str]
    copyright_text: Optional[str] = Field(
        default=None,
        alias="copyrightText",
        description=(
            "The text of copyright declarations recited in the package, file or"
            " snippet.\n\nIf the copyrightText field is not present, it implies an"
            " equivalent meaning to NOASSERTION."
        ),
    )
    file_contributors: Optional[list[str]] = Field(
        default=None,
        alias="fileContributors",
        description=(
            "This field provides a place for the SPDX file creator to record file"
            " contributors. Contributors could include names of copyright holders"
            " and/or authors who may not be copyright holders yet contributed to the"
            " file content."
        ),
    )
    file_dependencies: Optional[list[str]] = Field(
        default=None,
        alias="fileDependencies",
        description=(
            "This field is deprecated since SPDX 2.0 in favor of using Section 7 which"
            " provides more granularity about relationships."
        ),
    )
    file_name: str = Field(
        ...,
        alias="fileName",
        description="The name of the file relative to the root of the package.",
    )
    file_types: Optional[list[FileType]] = Field(
        default=None, alias="fileTypes", description="The type of the file."
    )
    license_comments: Optional[str] = Field(
        default=None,
        alias="licenseComments",
        description=(
            "The licenseComments property allows the preparer of the SPDX document to"
            " describe why the licensing in spdx:licenseConcluded was chosen."
        ),
    )
    license_concluded: Optional[str] = Field(
        default=None,
        alias="licenseConcluded",
        description=(
            "License expression for licenseConcluded. See SPDX Annex D for the license"
            " expression syntax.  The licensing that the preparer of this SPDX document"
            " has concluded, based on the evidence, actually applies to the SPDX"
            " Item.\n\nIf the licenseConcluded field is not present for an SPDX Item,"
            " it implies an equivalent meaning to NOASSERTION."
        ),
    )
    license_info_in_files: Optional[list[str]] = Field(
        default=None,
        alias="licenseInfoInFiles",
        description=(
            "Licensing information that was discovered directly in the subject file."
            " This is also considered a declared license for the file.\n\nIf the"
            " licenseInfoInFile field is not present for a file, it implies an"
            " equivalent meaning to NOASSERTION."
        ),
    )
    notice_text: Optional[str] = Field(
        default=None,
        alias="noticeText",
        description=(
            "This field provides a place for the SPDX file creator to record potential"
            " legal notices found in the file. This may or may not include copyright"
            " statements."
        ),
    )


class Annotation3(Annotation):
    pass


class EndPointer(BaseModel):
    class Config:
        extra = Extra.forbid

    reference: str = Field(..., description="SPDX ID for File")
    offset: Optional[int] = Field(default=None, description="Byte offset in the file")
    line_number: Optional[int] = Field(
        default=None, alias="lineNumber", description="line number offset in the file"
    )


class StartPointer(EndPointer):
    pass


class Range(BaseModel):
    class Config:
        extra = Extra.forbid

    end_pointer: EndPointer = Field(..., alias="endPointer")
    start_pointer: StartPointer = Field(..., alias="startPointer")


class Snippet(BaseModel):
    class Config:
        extra = Extra.forbid

    spdxid: str = Field(
        ...,
        alias="SPDXID",
        description=(
            "Uniquely identify any element in an SPDX document which may be referenced"
            " by other elements."
        ),
    )
    annotations: Optional[list[Annotation3]] = Field(
        default=None, description="Provide additional information about an SpdxElement."
    )
    attribution_texts: Optional[list[str]] = Field(
        default=None,
        alias="attributionTexts",
        description=(
            "This field provides a place for the SPDX data creator to record"
            " acknowledgements that may be required to be communicated in some"
            " contexts. This is not meant to include the actual complete license text"
            " (see licenseConculded and licenseDeclared), and may or may not include"
            " copyright notices (see also copyrightText). The SPDX data creator may use"
            " this field to record other acknowledgements, such as particular clauses"
            " from license texts, which may be necessary or desirable to reproduce."
        ),
    )
    comment: Optional[str]
    copyright_text: Optional[str] = Field(
        default=None,
        alias="copyrightText",
        description=(
            "The text of copyright declarations recited in the package, file or"
            " snippet.\n\nIf the copyrightText field is not present, it implies an"
            " equivalent meaning to NOASSERTION."
        ),
    )
    license_comments: Optional[str] = Field(
        default=None,
        alias="licenseComments",
        description=(
            "The licenseComments property allows the preparer of the SPDX document to"
            " describe why the licensing in spdx:licenseConcluded was chosen."
        ),
    )
    license_concluded: Optional[str] = Field(
        default=None,
        alias="licenseConcluded",
        description=(
            "License expression for licenseConcluded. See SPDX Annex D for the license"
            " expression syntax.  The licensing that the preparer of this SPDX document"
            " has concluded, based on the evidence, actually applies to the SPDX"
            " Item.\n\nIf the licenseConcluded field is not present for an SPDX Item,"
            " it implies an equivalent meaning to NOASSERTION."
        ),
    )
    license_info_in_snippets: Optional[list[str]] = Field(
        default=None,
        alias="licenseInfoInSnippets",
        description=(
            "Licensing information that was discovered directly in the subject snippet."
            " This is also considered a declared license for the snippet.\n\nIf the"
            " licenseInfoInSnippet field is not present for a snippet, it implies an"
            " equivalent meaning to NOASSERTION."
        ),
    )
    name: str = Field(..., description="Identify name of this SpdxElement.")
    ranges: list[Range] = Field(
        ...,
        description=(
            "This field defines the byte range in the original host file (in X.2) that"
            " the snippet information applies to"
        ),
        min_items=1,
    )
    snippet_from_file: str = Field(
        ...,
        alias="snippetFromFile",
        description=(
            "SPDX ID for File.  File containing the SPDX element (e.g. the file"
            " contaning a snippet)."
        ),
    )


class RelationshipType(str, Enum):
    variant_of = "VARIANT_OF"
    copy_of = "COPY_OF"
    patch_for = "PATCH_FOR"
    test_dependency_of = "TEST_DEPENDENCY_OF"
    contained_by = "CONTAINED_BY"
    data_file_of = "DATA_FILE_OF"
    optional_component_of = "OPTIONAL_COMPONENT_OF"
    ancestor_of = "ANCESTOR_OF"
    generates = "GENERATES"
    contains = "CONTAINS"
    optional_dependency_of = "OPTIONAL_DEPENDENCY_OF"
    file_added = "FILE_ADDED"
    requirement_description_for = "REQUIREMENT_DESCRIPTION_FOR"
    dev_dependency_of = "DEV_DEPENDENCY_OF"
    dependency_of = "DEPENDENCY_OF"
    build_dependency_of = "BUILD_DEPENDENCY_OF"
    describes = "DESCRIBES"
    prerequisite_for = "PREREQUISITE_FOR"
    has_prerequisite = "HAS_PREREQUISITE"
    provided_dependency_of = "PROVIDED_DEPENDENCY_OF"
    dynamic_link = "DYNAMIC_LINK"
    described_by = "DESCRIBED_BY"
    metafile_of = "METAFILE_OF"
    dependency_manifest_of = "DEPENDENCY_MANIFEST_OF"
    patch_applied = "PATCH_APPLIED"
    runtime_dependency_of = "RUNTIME_DEPENDENCY_OF"
    test_of = "TEST_OF"
    test_tool_of = "TEST_TOOL_OF"
    depends_on = "DEPENDS_ON"
    specification_for = "SPECIFICATION_FOR"
    file_modified = "FILE_MODIFIED"
    distribution_artifact = "DISTRIBUTION_ARTIFACT"
    amends = "AMENDS"
    documentation_of = "DOCUMENTATION_OF"
    generated_from = "GENERATED_FROM"
    static_link = "STATIC_LINK"
    other = "OTHER"
    build_tool_of = "BUILD_TOOL_OF"
    test_case_of = "TEST_CASE_OF"
    package_of = "PACKAGE_OF"
    descendant_of = "DESCENDANT_OF"
    file_deleted = "FILE_DELETED"
    expanded_from_archive = "EXPANDED_FROM_ARCHIVE"
    dev_tool_of = "DEV_TOOL_OF"
    example_of = "EXAMPLE_OF"


class Relationship(BaseModel):
    class Config:
        extra = Extra.forbid

    spdx_element_id: str = Field(
        ...,
        alias="spdxElementId",
        description="Id to which the SPDX element is related",
    )
    comment: Optional[str]
    related_spdx_element: str = Field(
        ...,
        alias="relatedSpdxElement",
        description="SPDX ID for SpdxElement.  A related SpdxElement.",
    )
    relationship_type: RelationshipType = Field(
        ...,
        alias="relationshipType",
        description="Describes the type of relationship between two SPDX elements.",
    )


class SPDXBom(BaseModel):
    class Config:
        extra = Extra.forbid

    spdxid: str = Field(
        ...,
        alias="SPDXID",
        description=(
            "Uniquely identify any element in an SPDX document which may be referenced"
            " by other elements."
        ),
    )
    annotations: Optional[list[Annotation]] = Field(
        default=None, description="Provide additional information about an SpdxElement."
    )
    comment: Optional[str]
    creation_info: CreationInfo = Field(
        ...,
        alias="creationInfo",
        description=(
            "One instance is required for each SPDX file produced. It provides the"
            " necessary information for forward and backward compatibility for"
            " processing tools."
        ),
    )
    data_license: str = Field(
        ...,
        alias="dataLicense",
        description=(
            "License expression for dataLicense. See SPDX Annex D for the license"
            " expression syntax.  Compliance with the SPDX specification includes"
            " populating the SPDX fields therein with data related to such fields"
            ' ("SPDX-Metadata"). The SPDX specification contains numerous fields where'
            " an SPDX document creator may provide relevant explanatory text in"
            ' SPDX-Metadata. Without opining on the lawfulness of "database rights" (in'
            " jurisdictions where applicable), such explanatory text is copyrightable"
            " subject matter in most Berne Convention countries. By using the SPDX"
            " specification, or any portion hereof, you hereby agree that any copyright"
            " rights (as determined by your jurisdiction) in any SPDX-Metadata,"
            " including without limitation explanatory text, shall be subject to the"
            " terms of the Creative Commons CC0 1.0 Universal license. For"
            " SPDX-Metadata not containing any copyright rights, you hereby agree and"
            ' acknowledge that the SPDX-Metadata is provided to you "as-is" and without'
            " any representations or warranties of any kind concerning the"
            " SPDX-Metadata, express, implied, statutory or otherwise, including"
            " without limitation warranties of title, merchantability, fitness for a"
            " particular purpose, non-infringement, or the absence of latent or other"
            " defects, accuracy, or the presence or absence of errors, whether or not"
            " discoverable, all to the greatest extent permissible under applicable"
            " law."
        ),
    )
    external_document_refs: Optional[list[ExternalDocumentRef]] = Field(
        default=None,
        alias="externalDocumentRefs",
        description=("Identify any external SPDX documents referenced within this SPDX document."),
    )
    has_extracted_licensing_infos: Optional[list[HasExtractedLicensingInfo]] = Field(
        default=None,
        alias="hasExtractedLicensingInfos",
        description=(
            "Indicates that a particular ExtractedLicensingInfo was defined in the"
            " subject SpdxDocument."
        ),
    )
    name: str = Field(..., description="Identify name of this SpdxElement.")
    revieweds: Optional[list[Reviewed]] = Field(default=None, description="Reviewed")
    spdx_version: str = Field(
        ...,
        alias="spdxVersion",
        description=(
            "Provide a reference number that can be used to understand how to parse and"
            " interpret the rest of the file. It will enable both future changes to the"
            " specification and to support backward compatibility. The version number"
            " consists of a major and minor version indicator. The major field will be"
            " incremented when incompatible changes between versions are made (one or"
            " more sections are created, modified or deleted). The minor field will be"
            " incremented when backwards compatible changes are made."
        ),
    )
    document_namespace: Optional[str] = Field(
        default=None,
        alias="documentNamespace",
        description=(
            "The URI provides an unambiguous mechanism for other SPDX documents to"
            " reference SPDX elements within this SPDX document."
        ),
    )
    document_describes: Optional[list[str]] = Field(
        default=None,
        alias="documentDescribes",
        description="Packages, files and/or Snippets described by this SPDX document",
    )
    packages: Optional[list[Package]] = Field(
        default=None, description="Packages referenced in the SPDX document"
    )
    files: Optional[list[File]] = Field(
        default=None, description="Files referenced in the SPDX document"
    )
    snippets: Optional[list[Snippet]] = Field(
        default=None, description="Snippets referenced in the SPDX document"
    )
    relationships: Optional[list[Relationship]] = Field(
        default=None, description="Relationships referenced in the SPDX document"
    )
