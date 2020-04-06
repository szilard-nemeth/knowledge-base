package com.szilardnemeth.codesnippets.spring.integration;

class ObjectMapperConfigParameters {
  public static String[] main(String[] args) {
    ObjectMapper objectMapper = new ObjectMapper();
    objectMapper.configure(org.codehaus.jackson.JsonParser.Feature.ALLOW_BACKSLASH_ESCAPING_ANY_CHARACTER, true)
    objectMapper.configure(JsonParser.Feature.ALLOW_UNQUOTED_CONTROL_CHARS,
        true);
  }

}
